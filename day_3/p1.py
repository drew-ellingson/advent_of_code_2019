import operator

with open('input.txt') as my_file:
    lines = my_file.readlines()

wires = [line.split(',') for line in lines]
wire_grid_points = {1: [(0, 0)], 2: [(0, 0)]}

direct_dict = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


''' take care of one instruction in the list for a given wire'''
def one_direction(wire, input_tuple, input_instruction):
    direction = input_instruction[0]
    magnitude = int(input_instruction[1:])

    current_position = input_tuple
    for x in range(1, magnitude+1):
        current_position = tuple(map(operator.add, current_position , direct_dict[direction]))
        wire_grid_points[wire].append(current_position)

    return wire_grid_points


'''resolve all instructions for a given wire'''
def all_instructions(wire, instruction_list, starting_tuple):
    current_tuple = starting_tuple
    for inst in instruction_list:
        wire_grid_points = one_direction(wire, current_tuple, inst)
        current_tuple = wire_grid_points[wire][-1]
    return wire_grid_points


all_instructions(1, wires[0], (0, 0))
all_instructions(2, wires[1], (0, 0))

intersection = list(set(wire_grid_points[1]) & set(wire_grid_points[2]))

intersection.remove((0, 0))

print(min([abs(x[0]) + abs(x[1]) for x in intersection]))
