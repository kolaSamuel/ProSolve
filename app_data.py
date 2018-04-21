"""
    manipulation of stored data, includes actions that
    get, modify, add, delete and search for data in
    the database (currently in .json format)
"""
import json
formula_data = "formulas.json"

with open(formula_data) as file:
    data = json.load(file)


class DataFormat(dict):

    def __init__(self):
        sections = [
            ("__comment__", None),
            ("no_of_formulas", 0),
            ("no_of_sections", 0),
            ("sections", None),
            ("formulas", None),
        ]
        dict.__init__(self, sections)


def get_formula(section, shape):
    formulas = data[section][shape]["formulas"]
    return formulas


def add_formula(section, shape, new_formulas):
    shape_data = data[section][shape]
    formulas = shape_data["formulas"]
    new_formulas = list(map(lambda x: x.lower(), new_formulas))
    count = len(new_formulas)

    # update info
    shape_data["no_of_formulas"] += count
    data[section]["no_of_formulas"] += count
    data["Info"]["no_of_formulas"] += count

    formulas.extend(new_formulas)
    with open(formula_data, "w") as new_file:
        json.dump(data, new_file, indent=2)
    pass
