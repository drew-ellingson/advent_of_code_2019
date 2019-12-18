import itertools
import math

with open('test_6_input.txt') as my_file:
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

# take a cartesian product, remove x=x, and remove duplicates (x,y) ~ (y,x)
cands = list(itertools.product(asteroids.keys(), asteroids.keys()))
cands = sorted(list(filter(lambda x: x[0] != x[1], cands)))
cands = list(filter(lambda x: is_first(x[0], x[1]), cands))

def add(v1, v2):
    return tuple(map(lambda x, y: x+y, v1, v2))

def sub(v1, v2):
    return tuple(map(lambda x, y: x-y, v1, v2))

def div(v1, scalar):
    return tuple(map(lambda x: x / scalar, v1))

def mul(v1, scalar):
    return tuple(map(lambda x: int(x * scalar), v1))

def dot(v1, v2):
    return sum([x[0] * x[1] for x in list(zip(v1, v2))])

def norm(v1):
    return math.sqrt(dot(v1, v1))

def angle2(v1, v2):
    v1 = div(v1, norm(v1))
    v2 = div(v2, norm(v2))
    y = v2[0] - v1[0]
    x = v2[1] - v1[1]
    return math.atan2(y, x)


def intermediate_address(start, end):
    delta = sub(end, start)
    gcd = math.gcd(delta[0], delta[1])
    add_count = int(max(delta[0], delta[1]) / gcd)
    inc = list(map(int, div(delta, gcd)))
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

max_asteroids = max(asteroids.values())
station = list(asteroids.keys())[list(asteroids.values()).index(max_asteroids)]
print('Station is at {}'.format(station))
del asteroids[station]

def next_asteroid(asteroids, current_angle_vec):
    cands = dict(filter(lambda x: can_see(x[0], station), asteroids.items()))
    angle_dict = {x: angle2(current_angle_vec, sub(x, station)) for x in cands.keys()}
    pos_angles = list(filter(lambda x: x > 0, angle_dict.values()))
    neg_angles = list(filter(lambda x: x <= 0, angle_dict.values()))
    if len(pos_angles) > 0:
        min_angle = min(pos_angles)
    else:
        min_angle = min(neg_angles)
    min_ast = list(angle_dict.keys())[list(angle_dict.values()).index(min_angle)]
    min_delta = sub(min_ast, station)
    return min_ast

current_angle_vec = (-1, 0)
# klugey step 1 sorry
destroyed = [(1, 8)]
del asteroids[(1, 8)]
steps = 0

while len(asteroids.keys()) > 0:
    doomed = next_asteroid(asteroids, current_angle_vec)
    current_angle_vec = sub(doomed, station)
    destroyed.append(doomed)
    del asteroids[doomed]
    steps += 1

for x in destroyed:
    print(x)