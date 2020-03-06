from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

# date, hits * 1e3, mis * 1e3
row_data = [
    (datetime(2020, 2, 18,  4, 0),    1,    1),
    (datetime(2020, 2, 18,  6, 0),    1,    1),
    (datetime(2020, 2, 18,  8, 0),    1, 18),
    (datetime(2020, 2, 18, 10, 0),    1, 18),
    (datetime(2020, 2, 18, 12, 0),    1, 18),
    (datetime(2020, 2, 18, 14, 0),    1, 18),
    (datetime(2020, 2, 18, 16, 0),    1, 18),
    (datetime(2020, 2, 18, 18, 0),    1, 18),
    (datetime(2020, 2, 18, 20, 0),    1, 18),
    (datetime(2020, 2, 18, 22, 0),    1, 18),
    (datetime(2020, 2, 19,  0, 0),    1, 18),
    (datetime(2020, 2, 19,  2, 0),    1, 18),
    (datetime(2020, 2, 19,  4, 0),    1, 18),
    (datetime(2020, 2, 19,  6, 0),    1, 18),
    (datetime(2020, 2, 19,  8, 0),    1, 18),
    (datetime(2020, 2, 19, 10, 0),    1, 18),
    (datetime(2020, 2, 19, 12, 0),    1, 18),
    (datetime(2020, 2, 19, 14, 0),    1, 18),
    (datetime(2020, 2, 19, 16, 0),    1, 18),
    (datetime(2020, 2, 19, 18, 0),    1, 18),
    (datetime(2020, 2, 19, 20, 0),    1, 18),
    (datetime(2020, 2, 19, 22, 0),    1, 18),
    (datetime(2020, 2, 20,  0, 0),    1, 18),
    (datetime(2020, 2, 20,  2, 0),    1, 18),
    (datetime(2020, 2, 20,  4, 0),    1, 18),
    (datetime(2020, 2, 20,  6, 0),    1, 18),
    (datetime(2020, 2, 20,  8, 0),    1, 18),
    (datetime(2020, 2, 20, 10, 0),    1, 18),
    (datetime(2020, 2, 20, 12, 0),    1, 18)
]

size = len(row_data)
t0 = row_data[0][0]

for x in range(0, 24, 2):
    print(x)