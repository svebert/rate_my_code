import tempfile
from pathlib import Path
from rate_my_code import run_pylint

def test_run_pylint_returns_output():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        test_file = tmp_path / "dummy.py"
        test_file.write_text("def foo():\n    return 42\n")

        score = run_pylint(test_file)
        assert isinstance(score, float)
        assert 0 <= score <= 10
