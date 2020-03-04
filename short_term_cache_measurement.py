from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

# date, hits * 1e3, mis * 1e3
row_data = [
    (datetime(2020, 2, 17, 15, 18),   1,  18),
    (datetime(2020, 2, 17, 15, 30),   4,  42),
    (datetime(2020, 2, 17, 16,  0),   8,  72),
    (datetime(2020, 2, 17, 16, 30),  17, 119),
    (datetime(2020, 2, 17, 17,  0),  30, 155),
    (datetime(2020, 2, 17, 17, 30),  48, 195),
    (datetime(2020, 2, 17, 18,  0),  69, 235),
    (datetime(2020, 2, 17, 19,  0), 123, 315),
    (datetime(2020, 2, 17, 20,  0), 184, 389),
    (datetime(2020, 2, 17, 21,  0), 260, 451),
    (datetime(2020, 2, 17, 22,  0), 314, 484),
    (datetime(2020, 2, 17, 22, 40), 392, 530),
    (datetime(2020, 2, 17, 23, 52), 412, 540),
    (datetime(2020, 2, 17, 23, 55), 455, 558),
    (datetime(2020, 2, 18,  0, 30), 535, 593),
    (datetime(2020, 2, 18,  1, 20), 566, 616),
    (datetime(2020, 2, 18,  2, 10), 646, 644),
    (datetime(2020, 2, 18,  3, 20), 736, 680)
]

size = len(row_data)
t0 = row_data[0][0]


def to_hours(dt):
    return dt.days/24 + dt.seconds/3600


time = [to_hours(r[0] - t0) for r in row_data]
hits = [r[1] for r in row_data]
miss = [r[2] for r in row_data]
n    = [hits[i] + miss[i] for i in np.arange(size)]

plt.plot(time, hits, 'ro', color = 'b')
plt.plot(time, miss, 'ro', color = 'g')
plt.plot(time,    n, 'bs', color = 'r')
plt.xlabel('time, hours')
plt.ylabel('count, 10^3')
plt.show()