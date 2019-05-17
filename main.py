from src.database import *
from src.defuzzification import *
from src.fuzzification import *

class Personal_buyer:
    def __init__(self, micro, videoCard, screen, price):
        self.micro = micro
        self.videoCard= videoCard
        self.screen = screen
        self.price = price
