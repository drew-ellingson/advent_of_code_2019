with open('input.txt') as input:
    lines = [int(line.strip()) for line in input.readlines()]

fuel = [int(line / 3) - 2 for line in lines]

print(sum(fuel))
