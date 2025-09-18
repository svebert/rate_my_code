from rate_my_code import rate_my_code

print(
    rate_my_code(
        """
# This is very Pythonic
class Foo:
    def __init__(self):
        self.bar = 42

    def __str__(self):
        return str(self.bar)

    def baz(self):
        return [x for x in range(5)]
"""
    )
)
