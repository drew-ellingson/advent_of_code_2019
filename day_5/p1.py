with open('input.txt') as my_file:
    lines = list(map(int, my_file.readline().split(',')))

input = 1
output = []

'''return the immediate or position value depending on mode in [0,1]'''
def im_pos(il, pos, mode):
    return il[il[pos]] if mode == 0 else il[pos]

'''transform the instruction to remove the immedate/position mode logic'''
def make_instruction(il, op):
    input_string = '{0:05d}'.format(il[op])
    op_code = int(input_string[-2:])

    # last param will always be position mode
    if op_code in [1, 2]:
        new_params = [im_pos(il, op+1, int(input_string[2])),
                      im_pos(il, op+2, int(input_string[1])),
                      il[op+3]]
    # write-to param always in position mode
    elif op_code == 3:
        new_params = [il[op+1]]
    elif op_code == 4:
        new_params = [im_pos(il, op+1, int(input_string[2]))]
    return op_code, new_params

'''perform one operation'''
def one_step(il, op):
    op_code, params = make_instruction(il, op)
    if op_code == 1:
        il[params[2]] = params[0] + params[1]
    elif op_code == 2:
        il[params[2]] = params[0] * params[1]
    elif op_code == 3:
        il[params[0]] = input
    elif op_code == 4:
        output.append(params[0])
    return il

op = 0

while lines[op] != 99:
    one_step(lines, op)
    op += 4 if lines[op] % 100 in [1, 2] else 2

print(output[-1])
