from src.database import *


def category_selector(x):
    """
    :param x:
    :param obj:
    :return:    dict: fuzzy value: category
    """
    if bad(x) > 0:
        return {"value": bad(x), "category": "bad"}
    elif regular(x) > 0:
        return {"value": regular(x), "category": "regular"}
    elif good(x) > 0:
        return {"value": good(x), "category": "good"}
    else:
        return {"value": veryGood(x), "category": "veryGood"}