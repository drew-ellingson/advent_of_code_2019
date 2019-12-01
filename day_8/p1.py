from collections import Counter

with open('input.txt') as my_file:
    input = my_file.readline()

def flatten(il):
    return [item for list in il for item in list]

width, height = 25, 6
layers = int(len(input)/width/height)

all_layers = {k: [[int(input[k*width*height + j*width + i])
                   for i in range(width)]
                  for j in range(height)]
              for k in range(layers)}

num_counts = {k: Counter(flatten(all_layers[k])) for k in all_layers.keys()}
min_zeros = min(num_counts[k][0] for k in num_counts.keys())

output_layer = dict(filter(lambda x: x[1][0] == min_zeros, num_counts.items()))

print([x[1] * x[2] for x in list(output_layer.values())][0])
