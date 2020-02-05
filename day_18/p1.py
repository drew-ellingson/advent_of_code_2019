with open('input.txt') as my_file:
    input_lines = [line.strip() for line in my_file.readlines()]

maze = [[lr for lr in ud] for ud in input_lines]

# need to remember to remove old keys / doors as I collect them.
def remove_invalid_doors(obj_list):
    valid_keys_and_doors = []
    for obj in obj_list:
        if obj == obj.lower():
            valid_keys_and_doors.append(obj)
            continue
        else:
            if obj.lower() not in obj_list:
                valid_keys_and_doors.append(obj)
                continue
            continue
    return valid_keys_and_doors

def get_valid_keys_and_doors(maze):
    no_struct = [col for row in maze for col in row]
    maze_keys = list(filter(lambda x: x not in ('#','.','@'), no_struct))
    valid_keys_and_doors = remove_invalid_doors(maze_keys)
    return(sorted(valid_keys_and_doors))

