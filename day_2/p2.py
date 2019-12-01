'''one addition or multiplication instruction'''
def one_step(il, op):
    if il[op] == 1:
        il[il[op+3]] = il[il[op+1]] + il[il[op+2]]
    elif il[op] == 2:
        il[il[op+3]] = il[il[op+1]] * il[il[op+2]]

    return il


done = False
for x in range(0, 100):
    for y in range(0, 100):
        with open('input.txt') as my_file:
            input = my_file.readline().split(',')
            input = list(map(lambda x: int(x), input))
        input[1] = x
        input[2] = y
        op = 0
        while input[op] != 99:
            one_step(input, op)
            op += 4
        if input[0] == 19690720:
            done = True
            print(100*x + y)
            break
    if done:
        break
