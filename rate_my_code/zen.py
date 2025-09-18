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

    # 5) Einfache vs komplexe Ausdrücke
    if any(op in code for op in [" and ", " or ", " not "]):
        count += 1
        notes.append("Logische Operatoren genutzt – Explicit is better than implicit.")

    # 6) String-Formatierungen
    if any(f in code for f in ["f'", 'f"']):
        count += 1
        notes.append("F-Strings erkannt – Beautiful is better than ugly.")

    # 7) Einzeilige if/else vermeiden
    if "else:" in code and code.count("\n") < 3:
        count += 1
        notes.append("Kurze Einzeiler if/else – Simple is better than complex.")

    # 8) Funktionen und Klassen
    if "def " in code or "class " in code:
        count += 1
        notes.append("Funktionen oder Klassen definiert – There should be one obvious way to do it.")

    # 9) Keine globalen Variablen
    if "global " in code:
        notes.append("Globale Variablen gefunden – Refuse the temptation to guess.")
    else:
        count += 1
        notes.append("Keine globalen Variablen – Good practice!")

    return count, notes
