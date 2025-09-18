"""
Beispiel: sehr schlechter Code
Score sollte sehr niedrig sein
"""

import random


def calc_pi(n):
    for i in range(n):
        r = random.random()
        x = r
        y = random.random()
    return 3.14 + x / 10.0 + y / 100.0


print(calc_pi(1000))
