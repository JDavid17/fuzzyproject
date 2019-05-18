from src.database import *
from src.defuzzification import Defuzzification
from src.aggregation import AggregationMethods
from src.aggregation import *
from src.utilis import category_selector as cs
from src.utilis import price_selector as pc

import sys
import matplotlib.pyplot as pypol

rules = [
    "micro_regular & videoCard_regular & price_regular",
    "micro_regular & videoCard_regular & price_veryGood",
    "micro_regular & videoCard_good & price_regular",
    "micro_regular & videoCard_veryGood & price_good",
    "micro_regular & videoCard_veryGood & price_veryGood",

    "micro_good & videoCard_regular & price_regular",
    "micro_good & videoCard_regular & price_good",
    "micro_good & videoCard_good & price_regular",
    "micro_good & videoCard_good & price_veryGood",
    "micro_good & videoCard_veryGood & price_regular",

    "micro_veryGood & videoCard_regular & price_regular",
    "micro_veryGood & videoCard_good & price_regular",
    "micro_veryGood & videoCard_veryGood & price_regular",
]

impl = [
    "Maybe",
    "No",
    "Yes",
    "Yes",
    "Maybe",

    "Maybe",
    "No",
    "Yes",
    "No",
    "Yes",

    "Maybe",
    "Yes",
    "Yes"
]


class Personal_buyer:
    def __init__(self, micro, videoCard, price):
        self.micro = cs(micro)
        self.videoCard = cs(videoCard)
        self.price = pc(price)
        self.buy = "No"

    def __str__(self):
        return "micro.value: {} - micro.category: {}\n" \
               "videoCard.value: {} - videoCard.category: {}\n" \
               "price.value: {} - price.category: {}\n".format(self.micro["value"], self.micro["category"],
                                                               self.videoCard["value"], self.videoCard["category"],
                                                               self.price["value"], self.price["category"])


if __name__ == "__main__":
    if len(sys.argv) > 3:
        print(sys.argv)
        micro_value = int(sys.argv[1])
        videoCard_value = int(sys.argv[2])
        price_value = int(sys.argv[3])
        Personal_buyer(micro_value, videoCard_value, price_value)
        values = {"micro_regular": micro_value,
                  "micro_good": micro_value,
                  "micro_veryGood": micro_value,
                  "videoCard_regular": videoCard_value,
                  "videoCard_good": videoCard_value,
                  "videoCard_veryGood": videoCard_value,
                  "price_regular": price_value,
                  "price_good": price_value,
                  "price_veryGood": price_value
                  }

        memb = {
            "micro_regular": regular,
            "micro_good": good,
            "micro_veryGood": veryGood,
            "videoCard_regular": regular,
            "videoCard_good": good,
            "videoCard_veryGood": veryGood,
            "price_regular": regular,
            "price_good": good,
            "price_veryGood": veryGood,
            "Yes": Yes,
            "No": No,
            "Maybe": Maybe
        }

        rules_results = []
        index_rules = [Rule(item.split(' ')) for item in rules]
        for item in index_rules:
            # temp = {k: memb[k](v) for k, v in values.items()}
            val = item.evaluate({k: memb[k](v) for k, v in values.items()})
            rules_results.append(val)

        # print(rules_results)

        m_x, m_y = AggregationMethods.Mamdani(impl, rules_results, memb, (0, 2))
        l_x, l_y = AggregationMethods.Larsen(impl, rules_results, memb, (0, 2))

        # print(m_x)
        # print(m_y)
        print("Defuzzification Using Centroid")
        print("Defuzzification for Mamdani using Centroide: " + str(Defuzzification.centroide(m_x, m_y)))
        print("Defuzzification for Larsen using Centroide: " + str(Defuzzification.centroide(l_x, l_y)))

        print("Defuzzification Using Bisection")
        print("Defuzzification for Mamdani using Bisection: " + str(Defuzzification.bisection(m_x, m_y)))
        print("Defuzzification for Larsen using Bisection: " + str(Defuzzification.bisection(l_x, l_y)))

        pypol.plot(m_x, m_y)
        pypol.plot(l_x, l_y)
        pypol.show()
    else:
        print('Introduzca bien los parametros, siguiendo este formato: \n'
              'Calidad del Micro: Int[1-30]\n'
              'Calidad de la Tarjeta de Video: Int[1-30]\n'
              'Caldiad del Precio: Int[1-30]\n'
              'EJemplo: python main.py 25 9 10')
    # micro_value = 25
    # videoCard_value = 9
    # price_value = 10
    # assistant = Personal_buyer(micro_value, videoCard_value, price_value, 'bisection')

    # categorys = {"micro": assistant.micro["category"],
    #              "videoCard": assistant.videoCard["category"],
    #              "price": assistant.price["category"]}
    # print(assistant.micro["value"])
    # print(assistant.micro["category"])
    # print(assistant.videoCard["value"])
    # print(assistant.videoCard["category"])
    # print(assistant.price["value"])
    # print(assistant.price["category"])
