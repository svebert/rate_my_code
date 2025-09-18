import pytest
from rate_my_code import rate_my_kot


def test_rate_my_kot_always_disgusting():
    result = rate_my_kot("whatever")
    assert "🤢" in result
