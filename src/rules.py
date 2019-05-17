"""
rules.py: Rule Base − It contains fuzzy IF-THEN rules.
"""


class AndOp:
    def __init__(self, x, y):
        self.name = "And"
        self.op = "Min"
        self.x = x
        self.y = y
        self.func = min(x, y)


class OrOp:
    def __init__(self, x, y):
        self.name = "Or"
        self.op = "Max"
        self.x = x
        self.y = y
        self.func = max(x, y)


class NotOp:
    def __init__(self, x):
        self.name = "Not"
        self.op = "Sub"
        self.x = x
        self.func = 1 - x