from math import pi
from collections import Counter
from utils import *


class Circle(object):

    def __init__(self, data):

        self.data = data
        self.loopTerminate = Counter()
        self.find = {"area": self.find_area,
                     "radius": self.find_radius}

    def find_area(self):
        radius = self.data["radius"]
        if not radius:
            self.loopTerminate["radius"] = 1
            self.find["radius"]()
            radius = self.data["radius"]

        if not radius:
            raise ValueError

    def find_radius(self):
        pass

    def __getitem__(self, query):

        if self.data[query]:
            return self.data[query]

        try:
            self.find[query]()
            self.loopTerminate = Counter()
            return self.data[query]
        except ValueError:
            insufficient_data_handler(query, self.data.copy())


shape_type = {"circle": Circle,
              }
