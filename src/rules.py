"""
rules.py: Rule Base − It contains evaluation for fuzzy IF-THEN rules.

Input variables and categories:
vars = {micro, videoCard, screen, price}

Categories:
micro = {regular, good, veryGood} => [1-30]

videoCard = {regular, good, veryGood} => [1-30]

price = {medium, high, veryHigh} => [1-30]
         bad  regular good  veryGood
"""
from copy import deepcopy


class Rule:
    def __init__(self, rule):
        self.rule = rule

    def evaluate(self, values):
        ruleValues = []
        for token in self.rule:
            if token != '&' and token != '|' and token != '~':
                ruleValues.append(values[token])
            else:
                ruleValues.append(token)

        return_list = []
        boolean = False
        for token in ruleValues:
            if token == '&' or token == '|':
                return_list.append(token)
            elif token == '~':
                boolean = True
            else:
                if boolean:
                    return_list.append(lambda x: 1 - token)
                    boolean = False
                else:
                    return_list.append(token)

        result = return_list[0]
        if len(return_list) > 1 and return_list[1] == '&':
            op = min
        else:
            op = max
        for i in range(2, len(return_list) - 2, 2):
            result = op(result, return_list[i])
            if return_list[i + 1] == '&':
                op = min
            else:
                op = max
        return op(result, return_list[len(return_list) - 1])