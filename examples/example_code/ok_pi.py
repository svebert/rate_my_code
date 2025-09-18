"""
Beispiel: ok-ish Code
Score sollte mittel sein (~6–7)
"""

import random


def monte_carlo_pi(n: int) -> float:
    """Berechnet Pi mit Monte-Carlo-Methode."""
    inside: int = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1.0:
            inside += 1
    return 4.0 * inside / n


if __name__ == "__main__":
    n_points: int = 10000
    print(f"Approximiertes Pi ({n_points} Punkte): {monte_carlo_pi(n_points):.6f}")
