
"""
Core text cleaning logic for Smart Punctuation & Whitespace Fixer.
This module is pure Python (no FastAPI imports) to keep it easy to test.
"""
from __future__ import annotations
import re
import unicodedata

# Precompiled regex patterns for speed
RE_CURLY_DOUBLE = re.compile(r'[“”]')
RE_CURLY_SINGLE = re.compile(r"[‘’]")
RE_MULTISPACE   = re.compile(r"\s+")
RE_DASH_FIX     = re.compile(r"\s-\s")  # space-hyphen-space

def clean_text(text: str) -> str:
    """
    Normalize and clean punctuation + whitespace without changing meaning.
    Steps:
      - Unicode normalize to NFKC
      - Convert curly quotes to straight quotes
      - Collapse repeated whitespace
      - Replace ' - ' with em dash '—' (light editorial tweak)
      - Trim leading/trailing whitespace
    """
    if text is None:
        return ""
    t = unicodedata.normalize("NFKC", text)
    t = RE_CURLY_DOUBLE.sub('"', t)
    t = RE_CURLY_SINGLE.sub("'", t)
    t = RE_MULTISPACE.sub(" ", t)
    t = RE_DASH_FIX.sub("—", t)
    t = t.strip()
    return t
