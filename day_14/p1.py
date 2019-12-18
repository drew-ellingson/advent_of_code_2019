import math

with open('input.txt') as my_file:
    input = [line.strip().split(' => ') for line in my_file.readlines()]

def _ingredients(ing):
    ings = ing.split(', ')
    ings_dict = {}
    for ing in ings:
        ing_name = ing[ing.index(' ')+1:]
        ing_quant = int(ing[:ing.index(' ')])
        ings_dict[ing_name] = ing_quant
    return ings_dict

recipes = [(_ingredients(x[0]), _ingredients(x[1])) for x in input]

requirements = {'FUEL': 1}

def reduce(_requirements):
    for chem in requirements.keys():
        if chem == 'ORE':
            continue
        amount = requirements[chem]
        new_reqs = list(filter(lambda x: x[1] == chem, recipes))
        rec_amount = new_reqs[1][chem]
        rec_quant = math.ceil(amount / rec_amount)
        for new_chem in new_reqs[0].keys():
            if new_chem in requirements.keys():
                requirements[new_chem] += rec_quant * new_reqs[new_chem]
            else:
                requirements[new_chem] = rec_quant * new_reqs[new_chem]
        requirements[chem] -= rec_quant * amount
