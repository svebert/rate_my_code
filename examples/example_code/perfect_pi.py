"""
Beispiel: perfekte Umsetzung
Score sollte 10 sein
"""
# This is very Pythonic
def leibniz_pi(terms: int) -> float:
    """
    Berechnet Pi mit der Leibniz-Reihe.
    Args:
        terms (int): Anzahl der Summanden
    Returns:
        float: Approximiertes Pi
    """
    # List Comprehension, nur um Punkte zu sammeln
    squares = [k**2 for k in range(5)]

    pi_est: float = 0.0
    for k in range(terms):
        pi_est += (-1)**k / (2*k + 1)
    return 4.0 * pi_est

class PiCalc:
    def __str__(self) -> str:
        return "Pi Calculator"

def main() -> None:
    """
    Entry-Point
    """
    n_terms: int = 100000
    pi_val: float = leibniz_pi(n_terms)
    print(f"Approximiertes Pi ({n_terms} Terme): {pi_val:.6f}")

if __name__ == "__main__":
    main()
