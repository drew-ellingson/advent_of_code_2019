input = '109165-576723'
pass_limits = list(map(lambda x: int(x), input.split('-')))
pass_range = range(pass_limits[0], pass_limits[1]+1)


def is_valid(candidate):
    candidate = str(candidate)
    repeating_val = False
    for x in range(len(candidate)-1):
        if candidate[x] > candidate[x+1]:
            return False
        if candidate[x] == candidate[x+1]:
            repeating_val = True
    if repeating_val:
        return True
    return False


valid_pass = list(filter(lambda x: is_valid(x), pass_range))

print(len(valid_pass))
