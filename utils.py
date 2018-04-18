"""
Various tools and utilities used
"""
from sympy import solve, sympify, Eq, symbols
from collections import defaultdict
from datascience import Table


class Node(Table):
    """
        pre- initialized table+ class
    """
    def __init__(self):
        labels = ['Equation', 'Symbols',
                  'Complexity']
        Table.__init__(self, labels=labels)
        self.all_children = set()

    def update(self, row, children):
        self.append(row)
        self.all_children.update(children)


class SolutionGraph(object):
    """
        A cyclic graph that connects all inter-related equations to themselves
        to convert problem into search problem.
    """

    def __init__(self, equations, data):
        """
            Initializes and builds solution graph, stores data(changing the
            data's "key identifiers" from string to symbols) and creates a set of
            all data already found or given.
        :param equations: array of string expressions
        :param data: already given data
        """
        # Initializations
        self.tree = defaultdict(Node)
        self.data = {symbols(variable): data[variable] for variable in data}
        self.data_set = set(self.data)

        # Build graph
        for equation in equations:
            self.add_equation(equation)

        # Magic, actually just organised children in order of likelihood
        for node in self.tree:
            self.tree[node].sort('Complexity')

    def add_equation(self, equation):
        """
        Converts input string expression to function and stores
        :param equation:
        :return:
        """
        try:
            lhs, rhs = equation.split('=')
            formula = Eq(symbols(lhs), sympify(rhs))
            variables = formula.free_symbols
            for variable in variables:
                new_formula = solve(formula, variable)[-1]

                # new_variables == no of variables in formula that are unknown
                new_variables = new_formula.free_symbols - self.data_set
                row = [new_formula, new_variables, len(new_variables)]

                # updates
                self.tree[variable].update(row, new_variables)

        except ValueError:
            print('Equation Error: Invalid expression ',
                  equation, '\n \t Ignoring expression...\n')
            pass

    def __getitem__(self, item):
        """
        Finds solution to query
        :param item: query as string
        :return:
        """
        query = symbols(item)

        if query in self.data_set:
            print('Redundant query, value already previously found as ',
                  self.data[query])

        visited = set()

    def __str__(self):
        string = ''
        for node in self.tree:
            string += "\n" + str(node) + " :\n" + self.tree[node].__str__() \
                      + '\n' + self.tree[node].all_children.__str__() + '\n'
        return string


def insufficient_data_handler(query, data):

    """
    Checks if data is accurate ,tries again if not and terminates if accurate
    :param query: variable to be calculated given data
    :param data: available information to evaluate query
    :return: 0 that terminates or any other value ( which indicates a re-solve)
    """

    data_changes = 0

    print("Insufficient data given to compute, ", query)
    response = input("Confirm data? Y/N \n").strip()

    if response[:1].capitalize() == "Y":
        print("Input in format: variable <space> value",
              "Type 'done' when complete", sep='\n')
        for key in data:
            print(key, "-> ", data[key])
        print()
        try:
            variable, value = input("Input: ").strip().split()
            variable.lower()
        except ValueError:
            variable = 'done'

        while variable != 'done':
            data_changes += 1
            data[variable] = int(value)
            try:
                variable, value = input("Input: ").strip().split()
                variable.lower()
            except ValueError:
                variable = 'done'

        if data_changes:
            print("Attempting to Re-Solve the problem...")

    return data_changes
