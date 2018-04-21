"""
    After question type and shape have been identified
    Calls geometry to assign proper shape to solve problem.
"""

from utils import *
from app_data import get_formula, add_formula

app_name = "Geometry"


class Circle(object):

    def __init__(self, data, find):
        """
        :param data: list of given data from question
        :param find: list of query's from question
        """
        shape = "Circle"
        self.formulas = get_formula(app_name, shape)

        # initialises formulas for SolutionGraph search
        self.find = SolutionGraph(self.formulas, data, find)

    def __getitem__(self, query):
        """
        Finds query buy searching through Solution graph
        :param query:
        :return:
        """
        return self.find[query]


shape_type = {"circle": Circle,
              }


def geometry(s_type, query):
    shape = shape_type[s_type]()
    return shape[query]
