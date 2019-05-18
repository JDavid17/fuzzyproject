"""
database.py: Database − It defines the membership functions of fuzzy sets used in fuzzy rules.

Input variables and categories:
vars = {micro, videoCard, price}

Categories:
micro = {regular, good, veryGood} => [1-30]

videoCard = {regular, good, veryGood} => [1-30]

price = {medium, high, veryHigh} => [1-30]
         bad  regular good  veryGood
"""

from src.membership import triangular_mf


def regular(x):
    if 1 <= x <= 10:
        return triangular_mf(x, 1, 10, 10)
    else:
        return 0


def good(x):
    if 11 <= x <= 20:
        return triangular_mf(x, 11, 20, 20)
    else:
        return 0


def veryGood(x):
    if 21 <= x <= 30:
        return triangular_mf(x, 21, 30, 30)
    else:
        return 0

def Yes(x):
    if 0.6 <= x <= 1:
        return triangular_mf(x, 0.6, 1, 1)
    else:
        return 0

def No(x):
    if 0.1 <= x <= 0.3:
        return triangular_mf(x, 0.1, 0.3, 0.3)
    else:
        return 0

def Maybe(x):
    if 0.4 <= x <= 0.5:
        return triangular_mf(x, 0.4, 0.5, 0.5)
    else:
        return 0