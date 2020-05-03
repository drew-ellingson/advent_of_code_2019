import itertools
import math

with open('input.txt') as my_file:
    input = [list(x.strip()) for x in my_file.readlines()]

height = len(input)
width = len(input[0])

asteroids = {(x, y): 0 for x in range(height)
        for y in range(width) if input[x][y] == '#'}

def is_first(start, stop):
    if start[0] < stop[0]:
        return True
    if start[0] == stop[0] and start[1] < stop[1]:
        return True
    return False

cands = list(itertools.product(asteroids.keys(), asteroids.keys()))
cands = sorted(list(filter(lambda x: x[0] != x[1], cands)))
cands = list(filter(lambda x: is_first(x[0], x[1]), cands))

def add(pt1, pt2):
    return tuple(map(lambda x, y: x+y, pt1, pt2))

def sub(pt1, pt2):
    return tuple(map(lambda x, y: x-y, pt1, pt2))

def div(pt1, scalar):
    return tuple(map(lambda x: int(x / scalar), pt1))

def mul(pt1, scalar):
    return tuple(map(lambda x: int(x * scalar), pt1))

def intermediate_address(start, end):
    delta = sub(end, start)
    gcd = math.gcd(delta[0], delta[1])
    add_count = int(max(delta[0], delta[1]) / gcd)
    inc = div(delta, gcd)
    all_ints = []
    current = start
    while add(current, inc) != end:
        current = add(current, inc)
        all_ints.append(current)
    return all_ints

def can_see(start, stop):
    block_cands = intermediate_address(start, stop)
    blockers = list(filter(lambda x: x in asteroids, block_cands))
    if len(blockers) > 0:
        return False
    return True

for (x, y) in cands:
    if can_see(x, y):
        asteroids[x] += 1
        asteroids[y] += 1

print(max(asteroids.values()))

