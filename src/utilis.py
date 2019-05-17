from src.database import *


def category_selector(x, obj):
    """
    :param x:
    :param obj:
    :return:    dict: fuzzy value: category
    """
    if bad(x) > 0:
        return {"value": bad(x), "category": obj + "_bad"}
    elif regular(x) > 0:
        return {"value": regular(x), "category": obj + "_regular"}
    elif good(x) > 0:
        return {"value": good(x), "category": obj + "_good"}
    else:
        return {"value": veryGood(x), "category": obj + "_veryGood"}