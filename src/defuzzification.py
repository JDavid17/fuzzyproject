"""
defuzzification.py : Defuzzification Interface Unit − It converts the fuzzy quantities into crisp quantities. 
"""
import numpy as np

def middle_index(i: int, l: list, old_l=float('-inf'), old_r=float('inf')):
    rigth = sum([l[idx] for idx in range(i, len(l))])
    left = sum(l) - rigth
    if rigth == left or abs(old_l - old_r) < abs(left - rigth) or i + 1 >= len(l) or i - 1 < 0:
        if abs(old_l - old_r) < abs(left - rigth):
            return i, old_l, old_r
        return i, left, rigth
    elif rigth > left:
        return middle_index(i + 1, l, left, rigth)
    return middle_index(i - 1, l, left, rigth)


class Defuzzification:
    @staticmethod
    def bisection(x: list, y: list):
        result, _, _ = middle_index(int(len(y) / 2), y)
        return x[result]

    @staticmethod
    def centroide(x: list, y: list):
        a = 0
        b = 0
        for i in range(len(x)):
            a += x[i] * y[i]
            b += y[i]
        return a / b

    @staticmethod
    def central_max(x: list, y: list):
        maxV = max(y)
        values = []
        for i in range(len(y)):
            if y[i] == maxV:
                values.append(x[i])
        return np.average(values)

    @staticmethod
    def min_max(x: list, y: list):
        return x[y.index(max(y))]

    @staticmethod
    def max_max(x: list, y: list):
        y.reverse()
        x.reverse()
        return Defuzzification.min_max(x, y)