import pytest
from rate_my_code import rate_my_code


def test_score_with_pythonic_comment():
    code = "# very Pythonic\nprint('hi')"
    result = rate_my_code(code)
    assert result["score"] > 5
    assert any("Pythonic" in c for c in result["comments"])


def test_list_comprehension_detected():
    code = "[x for x in range(10)]"
    result = rate_my_code(code)
    assert any("List Comprehension" in c for c in result["comments"])


def test_dunder_function_detected():
    code = "def __init__(self): pass"
    result = rate_my_code(code)
    assert result["score"] >= 1
    assert any("Dunder" in c for c in result["comments"])


def test_score_is_between_0_and_10():
    code = "print('hello world')"
    result = rate_my_code(code)
    assert 0 <= result["score"] <= 10
