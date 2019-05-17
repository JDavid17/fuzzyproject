"""
database.py: Database − It defines the membership functions of fuzzy sets used in fuzzy rules.

Input variables and categories:
vars = {micro, videoCard, screen, price}

Categories:
micro = {bad, regular, good, veryGood} => [1-40]

videoCard = {bad, regular, good, veryGood} => [1-40]

screen = {bad, regular, good, veryGood} => [1-40]
         
price = {low, medium, high, veryHigh} => [1-40]
         bad  regular good  veryGood
"""

from src.membership import triangular_mf


def bad(x):
    if 1 <= x <= 10:
        return triangular_mf(x, 1, 40, 40)
    else:
        return 0


def regular(x):
    if 11 <= x <= 20:
        return triangular_mf(x, 1, 40, 40)
    else:
        return 0


def good(x):
    if 21 <= x <= 30:
        return triangular_mf(x, 1, 40, 40)
    else:
        return 0


def veryGood(x):
    if 31 <= x <= 40:
        return triangular_mf(x, 1, 40, 40)
    else:
        return 0

