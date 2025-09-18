def zen_score(code: str) -> tuple[int, list[str]]:
    """
    Witzige Heuristik, die Code am 'Zen of Python' misst.
    """
    notes = []
    score = 0

    if "import" in code:
        score += 1
        notes.append("Namespaces are one honking great idea – schön importiert!")

    if code.count("    ") > 10:  # Viele Indents
        score -= 1
        notes.append(
            "Sehr tief verschachtelt. Flat is better than nested… just saying."
        )

    if "#" in code:
        score += 1
        notes.append("Kommentare gefunden – Readability counts!")

    if "try:" in code and "except:" in code:
        notes.append("Fehlerbehandlung ist da, aber Errors should never pass silently.")

    return score, notes
