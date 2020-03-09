with open('input.txt') as my_file:
    lines = [x.strip() for x in my_file.readlines()]
    grid = [[x for x in row] for row in lines]

grid_seq = [grid]

for x in grid:
    print(x)

print('apply a process')

def next_grid(grid):
    width = len(grid[0])
    height = len(grid)
    output = [[0 for x in range(width)] for y in range(height)]

    def next_grid_one_addr(col, row):
        bug_status = True if grid[col][row] == '#' else False
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        adjacents = []
        for x in directions:
            if col+x[1] <= width and col+x[1] >= 0 and row+x[0] <= height and row+x[0] >= 0:
                adjacents.append(grid[col+x[1]][row+x[0]])
        adjacent_bug_count = adjacents.count('#')
        return adjacent_bug_count
        # if bug_status and adjacent_bug_count == 1:
        #     return '#'
        # elif bug_status and adjacent_bug_count != 1:
        #     return '.'
        # elif not bug_status and adjacent_bug_count in [1, 2]:
        #     return '#'
        # else:
        #     return '.'
    
    for y in range(height):
        for x in range(width):
            output[y][x] = next_grid_one_addr(y,x)
            
    return output

successor = next_grid(grid)
for x in successor:
    print(x)