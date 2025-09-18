import pytest
from rate_my_code import rate_my_cod


def test_rate_my_cod_returns_string():
    result = rate_my_cod("fish.png")
    assert isinstance(result, str)
    assert "Cod" in result or "❌" in result
