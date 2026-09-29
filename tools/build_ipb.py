#!/usr/bin/env python3
"""Fill the official PWr SzD template ipb.docx from content/*.md.

Usage (from the repo root):
    python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt
    .venv/bin/python tools/build_ipb.py [--no-pdf]

Output:
    output/IPB_Grzegorz_Piotrowski.docx
    output/IPB_Grzegorz_Piotrowski.pdf   (LibreOffice `soffice --headless`; on macOS
                                         falls back to Pages.app; skipped if neither exists)
and a page-limit report on stdout: an estimate from text length for every limited
section, plus the height measured in the PDF when one was made and pypdf is installed.

LibreOffice gives the layout closest to Word. To install it on macOS:
    brew install --cask libreoffice

The template is document-protected (read-only with editable "permStart/permEnd"
regions). All text is written inside those regions, so the output stays editable
in Word exactly where the form allows it. ipb.docx and content/ are only read.
"""

from __future__ import annotations

import argparse
import copy
import re
import shutil
import subprocess
import sys
from pathlib import Path

import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "ipb.docx"
CONTENT = ROOT / "content"
OUTDIR = ROOT / "output"
OUTNAME = "IPB_Grzegorz_Piotrowski"

# Page-limit estimate parameters: A4, 2.5 cm margins, Calibri 11 pt, single spacing.
TEXT_WIDTH_PT = (21.0 - 2 * 2.5) / 2.54 * 72  # ~453.5 pt
TEXT_HEIGHT_PT = (29.7 - 2 * 2.5) / 2.54 * 72  # ~700 pt
AVG_CHAR_PT = 5.15  # average Calibri 11 pt glyph advance for mixed PL/EN prose
LINE_PT = 13.4  # Calibri 11 pt, line spacing 1
PARA_AFTER_TWIPS = 120  # 6 pt between paragraphs of filled-in text
PAGE_LIMITS = {5: 1, 6: 2, 7: 1, 8: 1, 9: 2, "10-PL": 1, "10-EN": 1, 12: 1}

NA_TEXT = "nie dotyczy / not applicable"
MARKER_RE = re.compile(r"TODO|UNVERIFIED|CONFIRM", re.I)


# --------------------------------------------------------------------------- markdown

def read_section(prefix: str) -> tuple[str, list[str]]:
    """Return (markdown without HTML comments and the '# §N' title, open-item markers)."""
    path = next(CONTENT.glob(f"{prefix}-*.md"))
    raw = path.read_text(encoding="utf-8")
    comments = re.findall(r"<!--(.*?)-->", raw, flags=re.S)
    markers = []
    for c in comments:
        for line in c.splitlines():
            if MARKER_RE.search(line):
                markers.append(f"{path.name}: {line.strip()[:110]}")
    text = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return "\n".join(lines).strip(), markers


def parse_blocks(md: str) -> list[tuple]:
    """Very small markdown block parser.

    Returns a list of ("p", text) | ("h", text) | ("li", marker, text) | ("table", rows).
    """
    blocks: list[tuple] = []
    para: list[str] = []
    lines = md.splitlines()
    i = 0

    def flush():
        if para:
            blocks.append(("p", " ".join(s.strip() for s in para)))
            para.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            flush()
            i += 1
            continue
        if s.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            blocks.append(("table", rows))
            continue
        m_h = re.match(r"#{1,6}\s+(.*)", s)
        m_li = re.match(r"([-*]|\d+\.)\s+(.*)", s)
        if m_h:
            flush()
            blocks.append(("h", m_h.group(1)))
        elif m_li and not line.startswith("  "):
            flush()
            marker = "•" if m_li.group(1) in "-*" else m_li.group(1)
            item = [m_li.group(2)]
            i += 1
            # continuation lines are indented and are not new list items
            while i < len(lines) and lines[i].startswith("  ") and lines[i].strip() \
                    and not re.match(r"\s*([-*]|\d+\.)\s", lines[i]):
                item.append(lines[i].strip())
                i += 1
            blocks.append(("li", marker, " ".join(item)))
            continue
        elif m_li:  # nested list item: render as an indented bullet
            flush()
            blocks.append(("li2", "–", m_li.group(2)))
        elif re.match(r"\[\d+\]\s", s):  # reference-list entry: one paragraph each
            flush()
            blocks.append(("ref", s))
        else:
            # a bold lead-in ("**RQ2.** ...") after a finished sentence starts a new paragraph
            if para and s.startswith("**") and re.search(r"[.?!:]$", para[-1].strip()):
                flush()
            para.append(s)
        i += 1
    flush()
    return blocks


INLINE_RE = re.compile(r"(\*\*.+?\*\*|(?<![\w*])\*[^*\s][^*]*?\*(?![\w*])|`[^`]+`|\[[^\]]+\]\([^)]+\))")


def inline_runs(text: str) -> list[tuple[str, bool, bool]]:
    """Split inline markdown into (text, bold, italic) runs."""
    out: list[tuple[str, bool, bool]] = []

    def walk(t: str, bold: bool, ital: bool):
        pos = 0
        for m in INLINE_RE.finditer(t):
            if m.start() > pos:
                out.append((t[pos:m.start()], bold, ital))
            tok = m.group(0)
            if tok.startswith("**"):
                walk(tok[2:-2], True, ital)
            elif tok.startswith("*"):
                walk(tok[1:-1], bold, True)
            elif tok.startswith("`"):
                out.append((tok[1:-1], bold, ital))
            else:  # [text](url) -> text
                walk(re.match(r"\[([^\]]+)\]", tok).group(1), bold, ital)
            pos = m.end()
        if pos < len(t):
            out.append((t[pos:], bold, ital))

    walk(text, False, False)
    return [r for r in out if r[0]]


def plain(text: str) -> str:
    return "".join(r[0] for r in inline_runs(text))


# --------------------------------------------------------------------------- OOXML helpers

def make_run(text: str, bold=False, italic=False, lang="en-US") -> OxmlElement:
    r = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    fonts = OxmlElement("w:rFonts")
    fonts.set(qn("w:cstheme"), "minorHAnsi")
    rpr.append(fonts)
    if bold:
        rpr.append(OxmlElement("w:b"))
    if italic:
        rpr.append(OxmlElement("w:i"))
    lg = OxmlElement("w:lang")
    lg.set(qn("w:val"), lang)
    rpr.append(lg)
    r.append(rpr)
    t = OxmlElement("w:t")
    t.set(qn("xml:space"), "preserve")
    t.text = text
    r.append(t)
    return r


def base_ppr(after: int = PARA_AFTER_TWIPS, ind: tuple[int, int] | None = None,
             jc: str = "both", keep_next=False) -> OxmlElement:
    ppr = OxmlElement("w:pPr")
    if keep_next:
        ppr.append(OxmlElement("w:keepNext"))
    sp = OxmlElement("w:spacing")
    sp.set(qn("w:after"), str(after))
    sp.set(qn("w:line"), "240")  # line spacing 1
    sp.set(qn("w:lineRule"), "auto")
    ppr.append(sp)
    if ind:
        el = OxmlElement("w:ind")
        el.set(qn("w:left"), str(ind[0]))
        el.set(qn("w:hanging"), str(ind[1]))
        ppr.append(el)
    if jc:
        j = OxmlElement("w:jc")
        j.set(qn("w:val"), jc)
        ppr.append(j)
    return ppr


def fill_runs(p, text: str, lang: str, prefix: str | None = None, force_bold=False):
    if prefix:
        p.append(make_run(prefix + "\t", lang=lang))
    for t, b, i in inline_runs(text):
        p.append(make_run(t, b or force_bold, i, lang))


def new_para(ppr) -> OxmlElement:
    p = OxmlElement("w:p")
    p.append(ppr)
    return p


def make_table(rows: list[list[str]], lang: str, widths: list[int] | None = None) -> OxmlElement:
    """Bordered table ('Tabela-Siatka' = Table Grid in the template), header row bold."""
    ncol = max(len(r) for r in rows)
    total = 9072
    widths = widths or [total // ncol] * ncol
    tbl = OxmlElement("w:tbl")
    tpr = OxmlElement("w:tblPr")
    st = OxmlElement("w:tblStyle")
    st.set(qn("w:val"), "Tabela-Siatka")
    tpr.append(st)
    tw = OxmlElement("w:tblW")
    tw.set(qn("w:w"), str(total))
    tw.set(qn("w:type"), "dxa")
    tpr.append(tw)
    lay = OxmlElement("w:tblLayout")
    lay.set(qn("w:type"), "fixed")
    tpr.append(lay)
    tbl.append(tpr)
    grid = OxmlElement("w:tblGrid")
    for w in widths:
        g = OxmlElement("w:gridCol")
        g.set(qn("w:w"), str(w))
        grid.append(g)
    tbl.append(grid)
    for ri, row in enumerate(rows):
        tr = OxmlElement("w:tr")
        for ci in range(ncol):
            tc = OxmlElement("w:tc")
            tcpr = OxmlElement("w:tcPr")
            w = OxmlElement("w:tcW")
            w.set(qn("w:w"), str(widths[ci]))
            w.set(qn("w:type"), "dxa")
            tcpr.append(w)
            tc.append(tcpr)
            p = new_para(base_ppr(after=0, jc="left"))
            fill_runs(p, row[ci] if ci < len(row) else "", lang, force_bold=(ri == 0))
            tc.append(p)
            tr.append(tc)
        tbl.append(tr)
    return tbl


def render_blocks(blocks, lang: str) -> list[OxmlElement]:
    """Turn parsed markdown blocks into w:p / w:tbl elements."""
    els: list[OxmlElement] = []
    for b in blocks:
        kind = b[0]
        if kind == "p":
            p = new_para(base_ppr())
            fill_runs(p, b[1], lang)
        elif kind == "h":
            p = new_para(base_ppr(after=60, jc="left", keep_next=True))
            fill_runs(p, b[1], lang, force_bold=True)
        elif kind in ("li", "li2"):
            ind = (284, 284) if kind == "li" else (568, 284)
            p = new_para(base_ppr(after=40, ind=ind))
            fill_runs(p, b[2], lang, prefix=b[1])
        elif kind == "ref":
            p = new_para(base_ppr(after=0, ind=(397, 397), jc="left"))
            fill_runs(p, b[1], lang)
        elif kind == "table":
            els.append(make_table(b[1], lang, table_widths(b[1])))
            p = new_para(base_ppr(after=0))  # spacer, also required after a table in a cell
        els.append(p)
    # last paragraph: no extra space after
    last = els[-1]
    if last.tag == qn("w:p"):
        last.find(qn("w:pPr")).find(qn("w:spacing")).set(qn("w:after"), "0")
    return els


def table_widths(rows):
    """Column widths (twips) proportional to content length, but never narrower than the
    column's longest word, so short cells like "1 (2025/26)" do not break mid-token."""
    total, pad = 9072, 250  # text width; cell margins + slack
    ncol = max(len(r) for r in rows)
    cols = [[plain(r[c]) if c < len(r) else "" for r in rows] for c in range(ncol)]
    floor = [max((len(w) for t in col for w in t.split()), default=1) * AVG_CHAR_PT * 20 * 1.1 + pad
             for col in cols]
    lens = [max(max(len(t) for t in col), 1) for col in cols]
    widths = [total * l / sum(lens) for l in lens]
    for _ in range(ncol):  # raise columns below their floor, take the space from the others
        low = [i for i in range(ncol) if widths[i] < floor[i]]
        if not low:
            break
        for i in low:
            widths[i] = floor[i]
        free = [i for i in range(ncol) if i not in low]
        rest = total - sum(widths[i] for i in low)
        share = sum(lens[i] for i in free) or 1
        for i in free:
            widths[i] = rest * lens[i] / share
    widths = [int(w) for w in widths]
    widths[-1] += total - sum(widths)
    return widths


# --------------------------------------------------------------------------- region filling

def perm_paragraphs(body):
    """Paragraph elements (body-level or inside tables) that contain a w:permStart."""
    return [p for p in body.iter(qn("w:p")) if p.find(qn("w:permStart")) is not None]


def fill_region(p, elements: list[OxmlElement]):
    """Replace the placeholder runs of paragraph `p` with `elements`.

    The first rendered paragraph's runs go into `p` itself (so permStart, bookmarks and
    the template's paragraph stay in place); remaining elements follow `p`. A permEnd
    that sat inside `p` is moved to the end of the last paragraph so the whole text
    stays inside the editable region.
    """
    for r in p.findall(qn("w:r")):
        p.remove(r)
    perm_end = p.find(qn("w:permEnd"))
    if perm_end is not None:
        p.remove(perm_end)
    first, rest = elements[0], elements[1:]
    if first.tag == qn("w:p"):
        # take the rendered paragraph's pPr but keep any existing rPr marker from the template
        new_ppr = first.find(qn("w:pPr"))
        old_ppr = p.find(qn("w:pPr"))
        if old_ppr is not None:
            p.remove(old_ppr)
        p.insert(0, new_ppr)
        anchor = p.find(qn("w:permStart"))
        idx = list(p).index(anchor) + 1 if anchor is not None else 1
        for r in first.findall(qn("w:r")):
            p.insert(idx, r)
            idx += 1
    else:
        rest = elements
    prev = p
    for el in rest:
        prev.addnext(el)
        prev = el
    if perm_end is not None:
        last_p = prev if prev.tag == qn("w:p") else None
        if last_p is None:
            last_p = new_para(base_ppr(after=0))
            prev.addnext(last_p)
        last_p.append(perm_end)


def set_text_run(p, text, bold=None, lang="en-US"):
    """Replace all runs of a single-line field paragraph with one run (keeps template rPr)."""
    runs = p.findall(qn("w:r"))
    rpr = copy.deepcopy(runs[0].find(qn("w:rPr"))) if runs and runs[0].find(qn("w:rPr")) is not None else None
    for r in runs:
        p.remove(r)
    new = make_run(text, bold=bool(bold), lang=lang)
    if rpr is not None:
        new.remove(new.find(qn("w:rPr")))
        new.insert(0, rpr)
        # drop grey/italic "e.g." styling if any
        for tag in ("w:i", "w:color"):
            el = rpr.find(qn(tag))
            if el is not None:
                rpr.remove(el)
    anchor = p.find(qn("w:permStart"))
    if anchor is not None:
        anchor.addnext(new)
    else:
        p.append(new)


def set_sdt_value(body, tag: str, value: str) -> str:
    """Select `value` in the combo box / dropdown content control with w:tag == tag."""
    for sdt in body.iter(qn("w:sdt")):
        pr = sdt.find(qn("w:sdtPr"))
        t = pr.find(qn("w:tag"))
        if t is None or t.get(qn("w:val")) != tag:
            continue
        lst = pr.find(qn("w:comboBox"))
        if lst is None:
            lst = pr.find(qn("w:dropDownList"))
        items = {li.get(qn("w:displayText")): li for li in lst.findall(qn("w:listItem"))}
        match = [k for k in items if k and k.strip() == value.strip()]
        if not match:
            raise SystemExit(f"'{value}' is not an option of content control '{tag}'")
        display = match[0]
        lst.set(qn("w:lastValue"), items[display].get(qn("w:value")))
        ph = pr.find(qn("w:showingPlcHdr"))
        if ph is not None:
            pr.remove(ph)
        content = sdt.find(qn("w:sdtContent"))
        runs = list(content.iter(qn("w:r")))
        first = runs[0]
        for r in runs[1:]:
            r.getparent().remove(r)
        rpr = first.find(qn("w:rPr"))
        if rpr is not None:
            rs = rpr.find(qn("w:rStyle"))  # placeholder-text character style
            if rs is not None:
                rpr.remove(rs)
        first.find(qn("w:t")).text = display
        return display
    raise SystemExit(f"content control with tag '{tag}' not found in template")


# --------------------------------------------------------------------------- page estimate

def est_lines(text: str, width_pt: float = TEXT_WIDTH_PT, indent_pt: float = 0) -> int:
    chars_per_line = max(10, int((width_pt - indent_pt) / AVG_CHAR_PT))
    n = len(text)
    return max(1, -(-n // chars_per_line))


def est_height(blocks) -> float:
    h = 0.0
    for b in blocks:
        if b[0] == "p":
            h += est_lines(plain(b[1])) * LINE_PT + PARA_AFTER_TWIPS / 20
        elif b[0] == "h":
            h += LINE_PT + 3
        elif b[0] == "ref":
            h += est_lines(plain(b[1]), indent_pt=20) * LINE_PT
        elif b[0] in ("li", "li2"):
            h += est_lines(plain(b[2]), indent_pt=14 if b[0] == "li" else 28) * LINE_PT + 2
        elif b[0] == "table":
            widths = table_widths(b[1])
            for row in b[1]:
                h += max(est_lines(plain(c), w / 20 - 11) for c, w in zip(row, widths)) * LINE_PT + 1
            h += LINE_PT
    return h


# --------------------------------------------------------------------------- main build

def build(make_pdf: bool = True) -> int:
    if not TEMPLATE.exists():
        raise SystemExit(f"template not found: {TEMPLATE}")
    doc = docx.Document(str(TEMPLATE))
    body = doc.element.body
    markers: list[str] = []
    report: list[tuple[str, float, int | None]] = []

    def section(prefix):
        md, mk = read_section(prefix)
        markers.extend(mk)
        return md

    # ---- §1 basic data (table 0, value column) ----
    md1 = section("01")
    fields = {}
    for b in parse_blocks(md1.split("## ")[0]):
        if b[0] == "table":
            for row in b[1][1:]:
                fields[plain(row[0]).split("/")[0].strip().lower()] = plain(row[1]).strip()

    def field(key):
        if key not in fields:
            raise SystemExit(f"§1 field '{key}' missing in content/01-basic-data.md")
        return fields[key]

    t0 = doc.tables[0]
    labels = [plain(r.cells[0].text).lower() for r in t0.rows]
    text_fields = {
        "imię i nazwisko": field("imię i nazwisko"),
        "katedra": field("katedra"),
        "data rozpoczęcia": field("data rozpoczęcia kształcenia"),
        "nr orcid": field("nr orcid"),
        "promotor/": field("promotor"),
        "promotor pomocniczy": field("promotor pomocniczy"),
    }
    assistant = text_fields["promotor pomocniczy"]
    has_assistant = assistant not in ("", "—", "-", "–", "brak", "none", "n/a")
    if not has_assistant:
        text_fields["promotor pomocniczy"] = "—"
    for key, val in text_fields.items():
        ri = next(i for i, l in enumerate(labels) if l.startswith(key))
        cell_p = t0.rows[ri].cells[1]._tc.find(qn("w:p"))
        set_text_run(cell_p, val, bold=True)
    disc = set_sdt_value(body, "SD", field("dyscyplina kształcenia"))
    fac = set_sdt_value(body, "Faculty", field("wydział"))

    # ---- locate free-text regions in body order ----
    body_perm = [p for p in perm_paragraphs(body) if p.getparent() is body]
    # body-level perm paragraphs in template order:
    # §2, §4, §5, §6, §7, §8, §9, §10-PL, §10-EN, §11, §12, §13, §14, sign..., date sdt, ...
    names = ["2", "4", "5", "6", "7", "8", "9", "10-PL", "10-EN", "11", "12", "13", "14"]
    regions = dict(zip(names, body_perm))

    def check_heading(pel, expect_prefix):
        """Sanity check: the nearest preceding numbered heading matches the section."""
        el = pel.getprevious()
        while el is not None:
            txt = "".join(t.text or "" for t in el.iter(qn("w:t"))).strip()
            if re.match(r"\d+\.", txt):
                if not txt.startswith(expect_prefix + "."):
                    raise SystemExit(f"template layout changed: region for §{expect_prefix} is under '{txt[:40]}'")
                return
            el = el.getprevious()

    for n, p in regions.items():
        check_heading(p, n.split("-")[0])

    # ---- §2 topic ----
    md2 = section("02")
    fill_region(regions["2"], render_blocks(parse_blocks(md2), "en-US"))

    # ---- §3 schedule (table 1) ----
    md3 = section("03")
    sched = next(b for b in parse_blocks(md3) if b[0] == "table")[1][1:]
    t1 = doc.tables[1]
    for row in sched:
        m = re.match(r"(\d)\s*(\((.*)\))?", plain(row[0]))
        sem, period = int(m.group(1)), m.group(3)
        desc = row[1].strip()
        # one paragraph per task: split before "**T<sem>.<n>**"
        parts = [s.strip() for s in re.split(r"(?=\*\*T\d\.\d\*\*)|\s(?=\d{1,2}\. [A-Z])", desc) if s and s.strip()]
        blocks = [("p", parts[0] if not period else f"*({period})* " + parts[0])] + [("p", s) for s in parts[1:]]
        els = render_blocks(blocks, "en-US")
        for e in els:
            e.find(qn("w:pPr")).find(qn("w:spacing")).set(qn("w:after"), "40")
            e.find(qn("w:pPr")).find(qn("w:jc")).set(qn("w:val"), "left")
        tr = next(r for r in t1.rows if r.cells[0].text.strip() == f"Semestr {sem}")
        cell_p = tr.cells[1]._tc.find(qn("w:p"))
        fill_region(cell_p, els)

    # ---- §4 date ----
    md4 = section("04")
    set_text_run(regions["4"], plain(md4).strip(), bold=True)

    # ---- §5–§9, §12, §13: free text ----
    limited = {"5": "05", "6": "06", "7": "07", "8": "08", "9": "09", "12": "12", "13": "13"}
    for n, prefix in limited.items():
        blocks = parse_blocks(section(prefix))
        if not blocks:  # empty section (e.g. §12 left blank, as the form allows)
            continue
        fill_region(regions[n], render_blocks(blocks, "en-US"))
        report.append((f"§{n}", est_height(blocks), PAGE_LIMITS.get(int(n))))

    # ---- §10 PL / EN ----
    md10 = section("10")
    halves = re.split(r"^##\s+.*$", md10, flags=re.M)
    heads = re.findall(r"^##\s+(.*)$", md10, flags=re.M)
    by_head = {h.strip().lower(): body_md.strip() for h, body_md in zip(heads, halves[1:])}
    pl = next(v for k, v in by_head.items() if k.startswith("streszczenie"))
    en = next(v for k, v in by_head.items() if k.startswith("abstract"))
    for key, text, lang in (("10-PL", pl, "pl-PL"), ("10-EN", en, "en-US")):
        blocks = parse_blocks(text)
        fill_region(regions[key], render_blocks(blocks, lang))
        report.append((f"§{key}", est_height(blocks), 1))

    # ---- §11 publication date ----
    blocks11 = parse_blocks(section("11"))
    fill_region(regions["11"], render_blocks(blocks11, "en-US"))

    # ---- §14 assistant supervisor ----
    if has_assistant:
        print(f"NOTE: assistant supervisor set ({assistant}); §14 left blank for their opinion.")
    else:
        set_text_run(regions["14"], NA_TEXT, bold=False)

    # ---- save ----
    OUTDIR.mkdir(exist_ok=True)
    out_docx = OUTDIR / f"{OUTNAME}.docx"
    doc.save(str(out_docx))

    # ---- validate by re-reading ----
    chk = docx.Document(str(out_docx))
    alltext = "\n".join(p.text for p in chk.paragraphs)
    celltext = "\n".join(c.text for t in chk.tables for r in t.rows for c in r.cells)
    for needle in (plain(md4).strip(), "research questions", "Streszczenie", "[1] "):  # "[1] " = §6 reference list present
        assert needle in alltext or needle in celltext, f"validation: '{needle}' missing in output"
    assert "Wybierz dyscyplinę" not in celltext and "Wybierz wydział" not in celltext
    print(f"Wrote {out_docx.relative_to(ROOT)}  (re-read OK: {len(chk.paragraphs)} paragraphs, "
          f"{len(chk.tables)} tables)")
    print(f"  §1 discipline: {disc}\n  §1 faculty:    {fac}")

    # ---- PDF (LibreOffice, or Pages.app on macOS) ----
    pdf, pdf_engine = None, None
    if make_pdf:
        pdf, pdf_engine = export_pdf(out_docx)
        if pdf:
            print(f"Wrote {pdf.relative_to(ROOT)}  (via {pdf_engine})")
        else:
            print("PDF: neither LibreOffice (soffice) nor Pages.app worked - skipped. Install LibreOffice "
                  "(e.g. `brew install --cask libreoffice`) to get a PDF and a measured page count.")
    measured, pdf_pages = measure_pdf(pdf) if pdf else ({}, None)

    # ---- page-limit report ----
    page_h = TEXT_HEIGHT_PT
    print("\nPage-limit report")
    print(f"  est.  = text-length estimate (Calibri 11 pt, spacing 1, A4, 2.5 cm margins, "
          f"~{int(TEXT_WIDTH_PT / AVG_CHAR_PT)} chars/line, ~{int(page_h / LINE_PT)} lines/page)")
    if measured:
        print(f"  PDF   = height measured in the {pdf_engine} PDF, in pages of {page_h:.0f} pt text height")
    elif pdf:
        print("  PDF   = not measured (install pypdf: pip install pypdf)")
    print(f"  {'section':<8}{'est.':>7}{'PDF':>7}{'limit':>7}  status")
    over = 0
    for name, h, limit in report:
        est = h / page_h
        meas = measured.get(name)
        pages = meas if meas is not None else est
        worst = max(est, meas or 0)
        if limit is None:
            status = "no limit"
        elif pages > limit:
            status, over = "OVER LIMIT - shorten", over + 1
        elif worst > limit:
            status = "RISK: over limit by one measure - check in Word"
        elif worst > 0.9 * limit:
            status = "close to limit - check in Word"
        else:
            status = "ok"
        m_txt = f"{meas:.2f}" if meas is not None else "-"
        print(f"  {name:<8}{est:>7.2f}{m_txt:>7}{(str(limit) if limit else '-'):>7}  {status}")
    if pdf_pages is not None:
        print(f"  Whole document ({pdf_engine} PDF): {pdf_pages} pages")
    else:
        print("  Whole document: no PDF, page count not measured")
    print("  Note: Word may lay out the text slightly differently; check the final layout in Word before printing.")

    if markers:
        print(f"\nOpen items in content/ HTML comments (not copied to the form): {len(markers)}")
        for m in markers:
            print("  - " + m)
    print("\n§15 date and signatures are left for signing by hand.")
    return over


def export_pdf(out_docx: Path) -> tuple[Path | None, str | None]:
    """Export the docx to PDF with LibreOffice; on macOS fall back to Pages.app via AppleScript."""
    pdf = out_docx.with_suffix(".pdf")
    if pdf.exists():
        pdf.unlink()  # never report on a stale PDF
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    mac_soffice = Path("/Applications/LibreOffice.app/Contents/MacOS/soffice")
    if not soffice and mac_soffice.exists():
        soffice = str(mac_soffice)
    if soffice:
        subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", str(pdf.parent),
                        str(out_docx)], check=True, capture_output=True, timeout=300)
        return (pdf, "LibreOffice") if pdf.exists() else (None, None)
    if sys.platform == "darwin" and Path("/Applications/Pages.app").exists():
        script = f"""
            set inFile to POSIX file "{out_docx}"
            set outFile to POSIX file "{pdf}"
            tell application "Pages"
                set d to open inFile
                delay 2
                export d to file outFile as PDF
                close d saving no
            end tell"""
        try:
            subprocess.run(["osascript", "-e", script], check=True, capture_output=True, timeout=300)
        except (subprocess.SubprocessError, OSError):
            return None, None
        return (pdf, "Pages.app") if pdf.exists() else (None, None)
    return None, None


def measure_pdf(pdf: Path) -> tuple[dict[str, float], int | None]:
    """Measure how many pages of text height each limited section takes in the PDF.

    A section's text runs from the line after its instruction paragraph (which ends with
    "line spacing 1).") to the last line before the next numbered heading; §10 is split at
    its "Streszczenie popularnonaukowe" / "Abstract for general public" labels. Needs pypdf.
    """
    try:
        import logging
        from pypdf import PdfReader
        logging.getLogger("pypdf").setLevel(logging.ERROR)
    except ImportError:
        return {}, count_pdf_pages(pdf)
    reader = PdfReader(str(pdf))
    chunks: list[tuple[int, float, str, bool]] = []  # (page, baseline y, text, bold)
    for pi, page in enumerate(reader.pages):
        def visit(text, cm, tm, font, size, pi=pi):
            if text.strip():
                name = str((font or {}).get("/BaseFont", ""))
                chunks.append((pi, float(cm[5]), text.strip(), "Bold" in name))
        page.extract_text(visitor_text=visit)
    # keep the body area only (drop header/footer page numbers) and restore reading order
    margin = 2.5 / 2.54 * 72
    top = float(reader.pages[0].mediabox.height) - margin
    chunks = [c for c in chunks if margin - 2 < c[1] < top + 12]
    chunks.sort(key=lambda c: (c[0], -round(c[1])))

    def heading(n: int, start: int = 0) -> int | None:
        for k in range(start, len(chunks)):
            if chunks[k][3] and re.match(rf"{n}\.(\s|$)", chunks[k][2]):
                return k
        return None

    def after(k: int, pred) -> int | None:
        for j in range(k, len(chunks)):
            if pred(chunks[j][2]):
                return j
        return None

    def next_line(k: int) -> int:
        j = k + 1
        while j < len(chunks) and (chunks[j][0], round(chunks[j][1])) == (chunks[k][0], round(chunks[k][1])):
            j += 1
        return j

    def span_pages(a: int, b: int) -> float:
        """Text height from chunk a to chunk b (inclusive), in pages."""
        by_page: dict[int, list[float]] = {}
        for pg, y, _, _ in chunks[a:b + 1]:
            by_page.setdefault(pg, []).append(y)
        h = sum(max(ys) - min(ys) + LINE_PT for ys in by_page.values())
        return h / TEXT_HEIGHT_PT

    out: dict[str, float] = {}
    for n in (5, 6, 7, 8, 9, 12, 13):
        h0, h1 = heading(n), heading(n + 1)
        if h0 is None or h1 is None:
            continue
        instr = after(h0, lambda t: t.endswith("spacing 1).")) if n != 13 else None
        start = next_line(instr) if instr is not None and instr < h1 else next_line(after(h0, lambda t: True) + 1)
        if n == 13:  # no page limit and no "spacing 1)." instruction; start after the description line
            start = next_line(after(h0, lambda t: t.endswith("communication.")) or h0)
        out[f"§{n}"] = span_pages(start, h1 - 1)
    h10, h11 = heading(10), heading(11)
    if h10 is not None and h11 is not None:
        instr = after(h10, lambda t: t.endswith("spacing 1)."))
        pl = after(instr, lambda t: t == "Streszczenie popularnonaukowe")
        en = after(pl or instr, lambda t: t == "Abstract for general public")
        if pl is not None and en is not None and en < h11:
            out["§10-PL"] = span_pages(next_line(pl), en - 1)
            out["§10-EN"] = span_pages(next_line(en), h11 - 1)
    return out, len(reader.pages)

def count_pdf_pages(pdf: Path) -> int | None:
    try:
        data = pdf.read_bytes()
    except OSError:
        return None
    m = re.findall(rb"/Type\s*/Pages\b[^>]*?/Count\s+(\d+)", data)
    if m:
        return max(int(x) for x in m)
    return len(re.findall(rb"/Type\s*/Page\b", data)) or None


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--no-pdf", action="store_true", help="skip the PDF export")
    ap.add_argument("--strict", action="store_true",
                    help="exit with status 1 if any section is over its page limit")
    args = ap.parse_args()
    n_over = build(make_pdf=not args.no_pdf)
    sys.exit(1 if (args.strict and n_over) else 0)
