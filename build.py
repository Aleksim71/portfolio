#!/usr/bin/env python3
"""Build a single self-contained HTML file from src/.

src/index.html references fonts/ and assets/ with relative paths, so it
works as-is in a browser and stays readable in the repository. This script
inlines every referenced file as a data: URI and writes dist/index.html -
one portable file with no external requests.

Usage: python3 build.py
"""
import base64
import mimetypes
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src" / "index.html"
OUT = ROOT / "dist" / "index.html"

mimetypes.add_type("font/woff2", ".woff2")
REF = re.compile(r"""(?P<q>['"])(?P<path>(?:assets|fonts)/[\w.-]+)(?P=q)""")


def inline(match):
    path = ROOT / "src" / match["path"]
    if not path.is_file():
        raise SystemExit(f"missing file referenced in index.html: {match['path']}")
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"{match['q']}data:{mime};base64,{data}{match['q']}"


def main():
    html = SRC.read_text(encoding="utf-8")
    built, count = REF.subn(inline, html)
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(built, encoding="utf-8")
    print(f"inlined {count} files -> {OUT.relative_to(ROOT)} ({OUT.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
