import re
import random
from .zen import zen_score


def rate_my_code(code: str) -> dict:
    """
    Analysiert Python-Code und gibt eine witzige Bewertung zurück.
    """

    score = 0
    comments = []

    # 1) Check auf "Pythonic"
    if "Pythonic" in code or "pythonic" in code.lower():
        score += 10
        comments.append("Kommentare mit 'Pythonic' sind wie Michelin-Sterne für Code.")

    # 2) List Comprehensions
    list_comps = len(re.findall(r"\[.*for.*in.*\]", code, flags=re.DOTALL))
    if list_comps > 0:
        score += list_comps * 2
        comments.append(f"{list_comps} List Comprehension(s) entdeckt – sehr elegant!")
    else:
        comments.append("Keine List Comprehensions? For-Loops sind sooo 90er…")

    # 3) Dunder Functions
    dunders = len(re.findall(r"def __\w+__", code))
    score += dunders
    if dunders > 0:
        comments.append(f"{dunders} Dunder-Methode(n) gefunden – Respekt, sehr OOP!")

    # 4) Zen of Python
    zenscore, zennotes = zen_score(code)
    score += zenscore
    comments.extend(zennotes)

    # 5) Zufallskomponente
    score += random.randint(-1, 1)

    # Normalize
    score = max(0, min(score, 10))

    return {"score": round(score, 2), "comments": comments}
