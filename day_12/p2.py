import itertools

with open('test_input.txt') as my_file:
    input = [line.strip().replace('<', '').replace('>', '').replace('x=', '')
             .replace('y=', '').replace('z=', '').split(', ') for
             line in my_file.readlines()]

position = {i: list(map(int, input[i])) for i in range(4)}
velocity = {i: [0, 0, 0] for i in position.keys()}

planet_hist = [{i: {'vel': velocity[i], 'pos': position[i]}
               for i in position.keys()}]

def calculate_vel(_position, _velocity):
    combs = itertools.product(_position.keys(), _position.keys())
    combs = list(filter(lambda x: x[0] < x[1], combs))
    for p1, p2 in combs:
        for i in range(3):
            if _position[p1][i] > _position[p2][i]:
                _velocity[p1][i] += -1
                _velocity[p2][i] += 1
            elif _position[p1][i] < _position[p2][i]:
                _velocity[p1][i] += 1
                _velocity[p2][i] += -1
    return _velocity

def update_position(_position, _velocity):
    _position = {i: [sum(x) for x in zip(_position[i], _velocity[i])] for i in _position.keys()}
    return _position

repeated = False
steps = 1
check_interval = 1000
while not repeated:
    velocity = calculate_vel(position, velocity)
    position = update_position(position, velocity)
    planet_hist.append({i: {'vel': velocity[i], 'pos': position[i]}
                        for i in position.keys()})
    if steps % check_interval == 0:
        print('starting check interval {}'.format(int(steps / check_interval)))
        # TODO figure out logic here
    steps += 1
