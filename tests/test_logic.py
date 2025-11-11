
from app.logic import clean_text

def test_basic_clean():
    messy = 'Here’s  a   sample— with  odd  spaces.\nLine breaks\r\nand “quotes”.'
    cleaned = clean_text(messy)
    assert '  ' not in cleaned
    assert '“' not in cleaned and '”' not in cleaned
    assert '’' not in cleaned and '‘' not in cleaned
    assert cleaned.startswith("Here's")

def test_none_safe():
    assert clean_text(None) == ""
