import re
from pathlib import Path
from typing import List, Optional, Dict, Any
from .zen import zen_count

# -----------------------------
# Einzelne Check-Funktionen (geben nur Counts zurück)
# -----------------------------


def count_pythonic_comments(code: str) -> int:
    """Zählt Kommentare mit 'Pythonic'."""
    return len(re.findall(r"#.*Pythonic", code, flags=re.IGNORECASE))


def count_list_comprehensions(code: str) -> int:
    """Zählt List Comprehensions."""
    return len(re.findall(r"\[.*for.*in.*\]", code, flags=re.DOTALL))


def count_dunder_functions(code: str) -> int:
    """Zählt Dunder-Methoden."""
    return len(re.findall(r"def __\w+__", code))


def count_zen_of_python_violations(code: str) -> int:
    """Zählt Zen-of-Python-Notizen (aus zen_score) als Count."""
    _, notes = zen_count(code)
    return len(notes)


# -----------------------------
# Score Berechnung pro Datei
# -----------------------------


def score_file(code: str) -> dict:
    """
    Berechnet Score für eine einzelne Datei.
    Gibt dict mit score, comments, length zurück.
    """
    length = len(code)
    counts = {
        "pythonic": count_pythonic_comments(code),
        "listcomp": count_list_comprehensions(code),
        "dunder": count_dunder_functions(code),
        "zen": count_zen_of_python_violations(code),
    }

    comments = []
    score = 0

    if counts["pythonic"] > 0:
        comments.append(f"{counts['pythonic']} Pythonic comment(s) gefunden")
        score += counts["pythonic"] * 5
    if counts["listcomp"] > 0:
        comments.append(f"{counts['listcomp']} List Comprehension(s) gefunden")
        score += counts["listcomp"] * 2
    if counts["dunder"] > 0:
        comments.append(f"{counts['dunder']} Dunder-Methode(n) gefunden")
        score += counts["dunder"] * 1
    if counts["zen"] > 0:
        comments.append(f"{counts['zen']} Zen-of-Python-Hinweis(e)")
        score += counts["zen"] * 1

    # Zufallsbonus
    import random

    score += random.randint(-1, 1)

    # Normalize pro file
    score = max(0, min(score, 10))

    return {"score": round(score, 2), "comments": comments, "length": length}


# -----------------------------
# Hauptfunktion für Pfad
# -----------------------------


def rate_my_code(path: Path, excludes: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Analysiert rekursiv alle .py-Dateien unter `path`
    und berechnet gewichteten Gesamt-Score.

    Args:
        path (Path | str): Basisverzeichnis des Packages.
        excludes (List[str], optional): Liste von exkludierten Ordnern
                                        Default ['.venv', '__pycache__'] ausgeschlossen.

    Returns:
        dict: {
            "score": float,               # gewichteter Gesamt-Score
            "files": {file_path: {...}},  # Score + Kommentare pro Datei
            "comments": list[str]         # gesammelte Hinweise aller Dateien
        }
    """
    if not isinstance(path, Path):
        path = Path(path)

    if excludes is None:
        excludes = [".venv", "__pycache__"]

    py_files = []
    for f in path.rglob("*.py"):
        # Prüfen, ob einer der excluded Ordner im Pfad ist
        if any(excl in f.parts for excl in excludes):
            continue
        py_files.append(f)

    if not py_files:
        return {"score": 0, "files": {}, "comments": []}

    files_scores = {}
    total_length = 0
    weighted_score_sum = 0
    all_comments = []

    for f in py_files:
        code = f.read_text(encoding="utf-8")
        result = score_file(code)  # score_file bleibt unverändert
        files_scores[str(f)] = result
        weighted_score_sum += result["score"] * result["length"]
        total_length += result["length"]
        all_comments.extend(result["comments"])

    # Gesamtgewichteter Score
    overall_score = weighted_score_sum / total_length if total_length > 0 else 0
    overall_score = round(overall_score, 2)

    return {"score": overall_score, "files": files_scores, "comments": all_comments}
