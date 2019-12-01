with open('input.txt') as my_file:
    input = my_file.readline().split(',')
    input = list(map(lambda x: int(x), input))

# given in problem
input[1] = 12
input[2] = 2


'''perform one addition or multiplication instruction'''
def one_step(il, op):
    if il[op] == 1:
        il[il[op+3]] = il[il[op+1]] + il[il[op+2]]
    elif il[op] == 2:
        il[il[op+3]] = il[il[op+1]] * il[il[op+2]]

    return il


op = 0

while input[op] != 99:
    one_step(input, op)
    op += 4

print(input[0])
