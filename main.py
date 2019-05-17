from src.database import *
from src.defuzzification import *
from src.fuzzification import *
from src.utilis import category_selector as cs


class Personal_buyer:
    def __init__(self, micro, videoCard, screen, price):
        self.micro = cs(micro, "micro")
        self.videoCard = cs(videoCard, "videoCard")
        self.screen = cs(screen, "screen")
        self.price = cs(price, "price")
