from src.database import *


def category_selector(x):
    """
    :param x:
    :return:    dict: fuzzy value: category
    """
    if regular(x) > 0:
        return {"value": regular(x), "category": "regular"}
    elif good(x) > 0:
        return {"value": good(x), "category": "good"}
    else:
        return {"value": veryGood(x), "category": "veryGood"}


def price_selector(x):
    if regular(x) > 0:
        return {"value": regular(x), "category": "medium"}
    elif good(x) > 0:
        return {"value": good(x), "category": "high"}
    else:
        return {"value": veryGood(x), "category": "veryHigh"}
