from math import pi
from collections import Counter
from utils import *


class Circle(object):

    def __init__(self, data):

        self.data = data
        self.loopTerminate = Counter()
        self.formulas = equation(['area = pi*radius**2',
                                  'diameter = 2*radius',
                                  'perimeter = 2*pi*r'
                                  ])

    def __getitem__(self, query):
        """
        Finds query buy checking through formulas to find relation
        :param query:
        :return:
        """
        pass


shape_type = {"circle": Circle,
              }
