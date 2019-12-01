with open('input.txt') as my_file:
    lines = list(map(lambda x: x.strip('\n'), my_file.readlines()))
    lines = [line.split(')') for line in lines]
    planets = {line[1]: line[0] for line in lines}

'''return a count of objects a planet is directly or indirectly orbiting'''
def ancestor_count(planet):
    if planet == 'COM':
        return 0
    else:
        return 1 + ancestor_count(planets[planet])

print(sum([ancestor_count(planet) for planet in planets.keys()]))