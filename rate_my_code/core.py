import re
import random
from .zen import zen_score

# -----------------------------
# Einzelne Check-Funktionen
# -----------------------------

def check_pythonic_comments(code: str) -> tuple[int, list[str]]:
    """Checkt auf 'Pythonic' Kommentare."""
    comments = []
    score = 0
    if "Pythonic" in code or "pythonic" in code.lower():
        score += 10
        comments.append("Kommentare mit 'Pythonic' sind wie Michelin-Sterne für Code.")
    return score, comments

def check_list_comprehensions(code: str) -> tuple[int, list[str]]:
    """Checkt auf List Comprehensions."""
    comments = []
    list_comps = len(re.findall(r"\[.*for.*in.*\]", code, flags=re.DOTALL))
    score = list_comps * 2
    if list_comps > 0:
        comments.append(f"{list_comps} List Comprehension(s) entdeckt – sehr elegant!")
    else:
        comments.append("Keine List Comprehensions? For-Loops sind sooo 90er…")
    return score, comments

def check_dunder_functions(code: str) -> tuple[int, list[str]]:
    """Checkt auf Dunder-Methoden."""
    comments = []
    dunders = len(re.findall(r"def __\w+__", code))
    score = dunders
    if dunders > 0:
        comments.append(f"{dunders} Dunder-Methode(n) gefunden – Respekt, sehr OOP!")
    return score, comments

def check_zen_of_python(code: str) -> tuple[int, list[str]]:
    """Checkt den Zen of Python."""
    return zen_score(code)

def check_random_bonus() -> tuple[int, list[str]]:
    """Gibt einen kleinen Zufallsbonus/malus."""
    return random.randint(-1, 1), []

# -----------------------------
# Hauptfunktion
# -----------------------------

def rate_my_code(code: str) -> dict:
    """
    Analysiert Python-Code und gibt eine witzige Bewertung zurück.
    """
    total_score = 0
    comments = []

    # Alle Checks nacheinander aufrufen
    for check in [
        check_pythonic_comments,
        check_list_comprehensions,
        check_dunder_functions,
        check_zen_of_python,
        check_random_bonus,
    ]:
        score, note = check(code) if check != check_random_bonus else check()
        total_score += score
        comments.extend(note)

    # Normalize
    total_score = max(0, min(total_score, 10))

    return {"score": round(total_score, 2), "comments": comments}
