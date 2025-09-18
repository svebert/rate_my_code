import pytest
from pathlib import Path
import tempfile
from rate_my_code import core

# Alias für die Hauptfunktion
rate_my_code = core.rate_my_code

# --------------------------
# Tests für die einzelnen count-Checks
# --------------------------


def test_count_pythonic_comments():
    code = "# Pythonic comment!"
    count = core.count_pythonic_comments(code)
    assert count > 0


def test_count_list_comprehensions():
    code = "[x for x in range(5)]"
    count = core.count_list_comprehensions(code)
    assert count > 0


def test_count_dunder_functions():
    code = "def __str__(self): pass"
    count = core.count_dunder_functions(code)
    assert count >= 1


def test_count_zen_of_python_violations(monkeypatch):
    # Zen-Score liefert tuple (score, notes)
    code = "some code"
    count = core.count_zen_of_python_violations(code)
    assert isinstance(count, int)


# --------------------------
# Tests für die Hauptfunktion (Pfad-basiert)
# --------------------------


def test_rate_my_code_single_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        file_path = tmp_path / "test.py"
        file_path.write_text(
            "# Pythonic\n[x for x in range(3)]\ndef __init__(self): pass"
        )

        result = rate_my_code(tmp_path)

        # Prüfe gewichteten Gesamt-Score
        assert 0 <= result["score"] <= 10

        # Prüfe, dass Datei erkannt wurde
        assert str(file_path) in result["files"]

        file_info = result["files"][str(file_path)]
        # Score pro Datei
        assert 0 <= file_info["score"] <= 10
        # Comments sollten vorhanden sein
        assert any("Pythonic" in c for c in file_info["comments"])
        assert any("List Comprehension" in c for c in file_info["comments"])
        assert any("Dunder" in c for c in file_info["comments"])


def test_rate_my_code_multiple_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        # Datei 1
        f1 = tmp_path / "f1.py"
        f1.write_text("# Pythonic\nprint('hi')")
        # Datei 2
        f2 = tmp_path / "f2.py"
        f2.write_text("[x for x in range(5)]\ndef __init__(self): pass")

        result = rate_my_code(tmp_path)

        # Prüfe gewichteten Gesamt-Score
        assert 0 <= result["score"] <= 10

        # Prüfe, dass beide Dateien erkannt wurden
        assert str(f1) in result["files"]
        assert str(f2) in result["files"]


def test_rate_my_code_on_package():
    """
    Testet die Hauptfunktion auf dem eigenen Package.
    Erwartet, dass einige .py-Dateien gefunden werden.
    """
    package_path = Path(__file__).parent.parent / "rate_my_code"
    result = core.rate_my_code(package_path)

    # Prüfen, dass mindestens eine Datei gefunden wurde
    assert len(result["files"]) > 0, "Es wurden keine Python-Dateien gefunden!"

    # Jede Datei hat Score 0–10 und mögliche Kommentare
    for f, info in result["files"].items():
        assert 0 <= info["score"] <= 10
        assert "length" in info
        assert isinstance(info["length"], int)
        assert "comments" in info
        assert isinstance(info["comments"], list)

    # Gesamt-Score liegt zwischen 0–10
    assert 0 <= result["score"] <= 10

    # Optional: Minimalanzahl an Dateien überprüfen
    # z.B. im Package selbst 6 Files
    assert (
        len(result["files"]) >= 6
    ), f"Zu wenige Dateien gefunden: {len(result['files'])}"
