"""
membership.py : Defines the membership functions of fuzzy sets used in fuzzy rules.
"""

def triangular_mf(x, a, b, c):
    """
        Triangular Membership Function:

        The parameters {a, b, c} (with a < b < c) determine the x coordinates 
        of the three corners of the underlying triangular MF
    """
    return max(min(x-a/b-a, c-x/c-b), 0)

def trapezoidal_mf(x, a, b, c, d):
    """
        Trapezoidal Membership Function:
        
        The parameters {a, b, c, d} (with a < b <= c < d) determine the x coordinates 
        of the four corners of the underlying trapezoidal MF.
    """
    return max(min(x-a/b-a, 1, d-x/d-c), 0)

# Customs