import itertools

with open('input.txt') as my_file:
    input = my_file.readline()
    input_list = [int(s) for s in input]

def pattern_maker(mask_length, repeat_count):
    base_pattern = [0, 1, 0, -1]
    pattern_block = list(itertools.chain.
                         from_iterable(itertools.repeat(x, repeat_count)
                                       for x in base_pattern))
    output = pattern_block

    while len(output) < mask_length + 1:
        output = output + pattern_block

    return output[1:mask_length + 1]

def output_list(input_list, index):
    mask = pattern_maker(len(input_list), index + 1)
    components = [a * b for (a, b) in zip(input_list, mask)]
    return abs(sum(components)) % 10


def one_phase(input_list):
    return [output_list(input_list, index) for index in range(len(input_list))]


def n_phases(input_list, n):
    for i in range(n):
        input_list = one_phase(input_list)
    return input_list

output = (n_phases(input_list,100))[0:8]

print(''.join([str(x) for x in output]))