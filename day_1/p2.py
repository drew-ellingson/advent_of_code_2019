with open('input.txt') as input:
    lines = [int(line.strip()) for line in input.readlines()]


'''input can be initial module weight or weight of fuel'''
def add_fuel(number):
    new_fuel = max(int(number/3) - 2, 0)
    return new_fuel

total_weight = [[line] for line in lines]

for weight in total_weight:
    while weight[-1] != 0:
        weight.append(add_fuel(weight[-1]))

# exclude module weights
fuel_weights = [sum(line[1:]) for line in total_weight]

print(sum(fuel_weights))
