"""
aggregation.py: Fuzzification Interface Unit − It converts the crisp quantities into fuzzy quantities.
                    Aggregation Methods
"""
from src.rules import Rule
from src.utilis import category_selector, price_selector

import numpy as np


class AggregationMethods:
    @staticmethod
    def Mamdani(implication, results, membership_function, space):
        values_x = []
        values_y = []
        for i in range(len(results)):
            for x in np.arange(space[0], space[1], 0.01):
                y = membership_function[implication[i]](x)

                result = y if results[i] >= y >= 0 else results[i]

                if x in values_x:
                    i_x = values_x.index(x)
                    values_y[i_x] = values_y[i_x] if values_y[i_x] > result else result
                else:
                    values_x.append(x)
                    values_y.append(result)

        return values_x, values_y

    @staticmethod
    def Larsen(implication, results, membership_function, space):
        values_x = []
        values_y = []
        for i in range(len(results)):
            for x in np.arange(space[0], space[1], 0.01):
                y = membership_function[implication[i]](x)
                result = y * results[i]
                if x in values_x:
                    i_x = values_x.index(x)
                    values_y[i_x] = values_y[i_x] if values_y[i_x] > result else result
                else:
                    values_x.append(x)
                    values_y.append(result)
        return values_x, values_y
