map = \
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

def recursive_find(i, j, size):
    if i >= 0 and i < map.shape[0] and j >= 0 and j < map.shape[1] and map[i][j]==1:
        size += 1
        map[i][j] = 2
        size = recursive_find(i, j - 1, size)
        size = recursive_find(i, j + 1, size)
        size = recursive_find(i - 1, j, size)
        size = recursive_find(i + 1, j, size)
    return size


import numpy as np
map = np.array(map)

sizes = []
for i in range(map.shape[0]):
    for j in range(map.shape[1]):
        size = 0
        size = recursive_find(i, j, size)
        sizes.append(size)

print(max(sizes))

