with open('input.txt') as my_file:
    input = my_file.readline()

width, height = 25, 6
layers = int(len(input)/width/height)

all_layers = {k: [[int(input[k*width*height + j*width + i])
                   for i in range(width)]
                  for j in range(height)]
              for k in range(layers)}

def get_value(row, column, all_layers):
    output_value = 2
    layer = 0
    while output_value == 2:
        output_value = all_layers[layer][row][column]
        layer += 1
    return output_value if output_value == 1 else ' '

output = [[get_value(j, i, all_layers)
           for i in range(width)]
          for j in range(height)]

for line in output:
    print(''.join(str(x) for x in line))
