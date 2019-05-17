from src.database import *

def category_selector(x, obj):
    if obj == "micro":
        if bad(x) > 0:
