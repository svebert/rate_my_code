import pytest
from rate_my_code import core

# Alias für die Hauptfunktion
rate_my_code = core.rate_my_code

# --------------------------
# Tests für die einzelnen checks
# --------------------------

def test_check_pythonic_comments():
    score, comments = core.check_pythonic_comments("# Pythonic!")
    assert score > 0
    assert any("Pythonic" in c for c in comments)

def test_check_list_comprehensions():
    code = "[x for x in range(5)]"
    score, comments = core.check_list_comprehensions(code)
    assert score > 0
    assert any("List Comprehension" in c for c in comments)

def test_check_dunder_functions():
    code = "def __str__(self): pass"
    score, comments = core.check_dunder_functions(code)
    assert score >= 1
    assert any("Dunder" in c for c in comments)

# --------------------------
# Tests für die Hauptfunktion
# --------------------------

def test_score_with_pythonic_comment():
    code = "# very Pythonic\nprint('hi')"
    result = rate_my_code(code)
    # Score sollte >5 sein (Pythonic Kommentar)
    assert result["score"] > 5
    # Kommentar sollte enthalten sein
    assert any("Pythonic" in c for c in result["comments"])

def test_list_comprehension_detected():
    code = "[x for x in range(10)]"
    result = rate_my_code(code)
    assert any("List Comprehension" in c for c in result["comments"])

def test_dunder_function_detected():
    code = "def __init__(self): pass"
    result = rate_my_code(code)
    # Score mindestens 1 wegen Dunder
    assert result["score"] >= 1
    assert any("Dunder" in c for c in result["comments"])

def test_score_is_between_0_and_10():
    code = "print('hello world')"
    result = rate_my_code(code)
    # Score immer im Bereich 0–10
    assert 0 <= result["score"] <= 10

