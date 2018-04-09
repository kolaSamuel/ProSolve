"""
    After question type and shape have been identified
    Calls geometry to assign proper shape to solve problem.
"""

from collections import Counter
from utils import *


class Circle(object):

    def __init__(self, data):

        self.data = data
        self.loopTerminate = Counter()
        self.formulas = []

        # initialises formulas for tree solution search
        equations(['area = pi*radius**2',
                   'diameter = 2*radius',
                   'perimeter = 2*pi*r',
                   ], self.formulas)

    def __getitem__(self, query):
        """
        Finds query buy checking through formulas to find relation
        :param query:
        :return:
        """
        pass


shape_type = {"circle": Circle,
              }


def geometry(s_type, query):
    shape = shape_type[s_type]()
    return shape[query]
