"""
Various tools and utilities used
"""
from sympy import solve, sympify, Eq, symbols
from collections import defaultdict
from datascience import Table
import sys

sys.setrecursionlimit(1000)


class SGNode(Table):
    """
        Solution Graph Node(SGNode), pre- initialized table+ class
    """
    def __init__(self):
        labels = ['Equation', 'Symbols',
                  'Complexity']
        Table.__init__(self, labels=labels)
        self.all_children = set()


class SolutionGraph(object):
    """
        A cyclic graph that connects all inter-related equations to themselves
        to convert problem into search problem.
    """

    def __init__(self, equations, data, find):
        """
            Initializes and builds solution graph, stores data( also changes the
            data's "keys" from string to symbols)
        :param equations: array of string expressions
        :param data: already given data
        :param find: list of query's
        """
        # Initializations
        self.tree = defaultdict(SGNode)
        self.data = {symbols(variable): data[variable] for variable in data}
        self.data_set = set(self.data)
        # Special tree Heuristic
        # Uses query list and data list to determine best path
        to_find = set([symbols(variable) for variable in find])
        self.all_data_set = self.data_set.union(to_find)

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
                new_variables = new_formula.free_symbols
                heuristic = len(new_variables-self.all_data_set)

                # **********Untested pruning Idea**********
                # if heuristic == len(new_variables):
                #     continue
                # *****************************************

                row = [new_formula, new_variables, heuristic]

                # updates on node
                self.tree[variable].append(row)

        except ValueError:
            print('Equation Error: Invalid expression ',
                  equation, '\n \t Ignoring expression...\n')
            pass

    def data_update(self, node, row):
        # calculate dependent variable given complete set of
        # independent variables in self.data
        self.data[node] = row.item("Equation").evalf(subs=self.data)
        self.data_set.add(node)
        self.all_data_set.add(node)

    def search(self, node, visited):
        """
        A* but looks like a dfs search
        :param node: current node
        :param visited: set of visited pairs
        :return: True or False, depending on if solvable or not
        """
        can_solve = False  # unnecessary initialization. Has no effect
        row_len = self.tree[node].num_rows
        for index in range(row_len):
            row = self.tree[node].row(index)

            # can be made faster somehow
            children = row.item("Symbols")
            can_solve = children.issubset(self.data_set)

            # update
            if can_solve:
                self.data_update(node, row)
                return can_solve

            for child in children:
                path = (node, child)
                if path in visited:
                    continue
                visited.add(path)
                can_solve = self.search(child, visited)

                # update
                if can_solve:
                    self.data_update(node, row)
                    return can_solve

        return can_solve

    def __getitem__(self, item):
        """
        Finds solution to query
        :param item: query as string
        :return:
        """
        query = symbols(item)

        if query in self.data_set:
            print('Redundant query,', query, 'already previously found as :', )
            return self.data[query]

        start_node = query
        visited = set()

        solution = self.search(start_node, visited)

        if solution:
            print(item.title(), "found! :")
            return self.data[query]
        else:
            insufficient_data_handler(item, self.data)

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
                variable = symbols(variable.lower())
            except ValueError:
                variable = 'done'

        if data_changes:
            print("Attempting to Re-Solve the problem...")

    return data_changes
