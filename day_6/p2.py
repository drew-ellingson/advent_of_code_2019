with open('input.txt') as my_file:
    lines = list(map(lambda x: x.strip('\n'), my_file.readlines()))
    lines = [line.split(')') for line in lines]
    planets = {line[1]: line[0] for line in lines}  # child: parent

santa_ancestors = ['COM']
you_ancestors = ['COM']

'''return a count of objects a planet is directly or indirectly orbiting'''
def ancestor_list(you_or_santa):
    planet = you_or_santa
    planet = planets[planet]
    while planet != 'COM':
        if you_or_santa == 'SAN':
            santa_ancestors.append(planet)
        else:
            you_ancestors.append(planet)
        planet = planets[planet]
    return santa_ancestors if you_or_santa == 'SAN' else you_ancestors

ancestor_list('SAN')
ancestor_list('YOU')

def diff(lista, listb):
    return [item for item in lista if item not in listb]

santa_uniques = diff(santa_ancestors, you_ancestors)
you_uniques = diff(you_ancestors, santa_ancestors)

# +1 for missed common item above, -1 since counting edges instead of vertices
print(len(santa_uniques) + len(you_uniques))