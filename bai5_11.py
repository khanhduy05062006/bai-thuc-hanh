
import numpy as np
data = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]
dtype = [('name', 'U20'), ('lop', 'i4'), ('chieucao', 'f4')]
arr = np.array(data, dtype=dtype)
sorted_arr = np.sort(arr, order=['lop', 'chieucao'])
print(sorted_arr)
