"""
membership.py : Defines the membership functions of fuzzy sets used in fuzzy rules.
"""


def triangular_mf(x, a, b, c):
    """
        Triangular Membership Function:

        The parameters {a, b, c} (with a < b < c) determine the x coordinates 
        of the three corners of the underlying triangular MF
    """
    if a <= x <= b:
        return (x - a) / (b - a)
    if b <= x <= c:
        return (c - x) / (c - b)
    return 0


def trapezoidal_mf(x, a, b, c, d):
    """
        Trapezoidal Membership Function:
        
        The parameters {a, b, c, d} (with a < b <= c < d) determine the x coordinates 
        of the four corners of the underlying trapezoidal MF.
    """
    if a <= x <= b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1
    elif c <= x <= d:
        return (d - x) / (d - c)
    else:
        return 0

def rating(x):
    """
    :param x: Value return from rule evaluation
    :return: Yes, No, Maybe
    """
    if 0 <= x <= 0.3:
        return "No"
    if 0.4 <= x <= 6:
        return "Maybe"
    if 0.7 <= x <= 1:
        return "Yes"


# Customs
# print(triangular_mf(0, 1, 40, 40))
# print(triangular_mf(5, 1, 40, 40))
# print(triangular_mf(10, 1, 40, 40))
# print(triangular_mf(15, 1, 40, 40))
# print(triangular_mf(20, 1, 40, 40))
# print(triangular_mf(25, 1, 40, 40))
# print(triangular_mf(30, 1, 40, 40))
# print(triangular_mf(35, 1, 40, 40))
# print(triangular_mf(40, 1, 40, 40))
