from src.database import *
from src.defuzzification import *
from src.fuzzification import *
from src.utilis import category_selector as cs


class Personal_buyer:
    def __init__(self, micro, videoCard, screen, price):
        self.micro = cs(micro)
        self.videoCard = cs(videoCard)
        self.screen = cs(screen)
        self.price = cs(price)

    def __str__(self):
        return "micro.value: {} - micro.category: {}\n" \
               "videoCard.value: {} - videoCard.category: {}\n" \
               "screen.value: {} - screen.category: {}\n" \
               "price.value: {} - price.category: {}\n".format(self.micro["value"], self.micro["category"],
                                                               self.videoCard["value"], self.videoCard["category"],
                                                               self.screen["value"], self.screen["category"],
                                                               self.price["value"], self.price["category"])


if __name__ == "__main__":
    assistant = Personal_buyer(35, 20, 10, 15)

    print(assistant)