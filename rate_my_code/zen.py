def zen_count(code: str) -> tuple[int, list[str]]:
    """
    Analysiert den Code nach Zen-of-Python-Mustern.
    Gibt die Anzahl gefundener Muster (count) und Hinweise zurück.
    """
    notes = []
    count = 0

    # 1) Imports als gutes Pattern
    if "import" in code:
        count += 1
        notes.append("Namespaces are one honking great idea – schön importiert!")

    # 2) Tiefe Verschachtelung
    if code.count("    ") > 10:  # Mehr als 10 Indents
        count += 1
        notes.append(
            "Sehr tief verschachtelt. Flat is better than nested… just saying."
        )

    # 3) Kommentare
    if "#" in code:
        count += 1
        notes.append("Kommentare gefunden – Readability counts!")

    # 4) Fehlerbehandlung
    if "try:" in code and "except:" in code:
        count += 1
        notes.append("Fehlerbehandlung erkannt – Errors should never pass silently.")

    return count, notes
