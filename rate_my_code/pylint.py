from pylint.lint import Run


def run_pylint(path) -> float:
    """
    Führt Pylint auf der Datei aus und gibt den globalen Score zurück (0–10).
    """
    results = Run([str(path)], exit=False)
    score = getattr(results.linter.stats, "global_note", 0.0)
    return float(score)  # <-- explizit in float konvertieren