import random


def rate_my_cod(image_path: str) -> str:
    """
    Erkenne einen Kabeljau (Cod) und gib Angel-Tipps zurück.
    Da wir keine echte Bilderkennung haben, wird zufällig entschieden.
    """

    fishes = ["Cod", "Hering", "Forelle", "Lachs", "Makrele"]
    chosen = random.choice(fishes)

    if chosen == "Cod":
        return "🐟 Das ist eindeutig ein Cod! Tipp: Mehr Würmer benutzen."
    else:
        return f"❌ Sorry, das sieht eher nach {chosen} aus. Kein Cod, kein Glück."
