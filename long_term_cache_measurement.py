from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

# date, hits * 1e3, mis * 1e3
row_data = [
    (datetime(2020, 2, 18,  4, 0),  774,  711),
    (datetime(2020, 2, 18,  6, 0),  878,  757),
    (datetime(2020, 2, 18,  8, 0), 1036,  826),
    (datetime(2020, 2, 18, 10, 0), 1231,  901),
    (datetime(2020, 2, 18, 12, 0), 1375,  969),
    (datetime(2020, 2, 18, 14, 0), 1490, 1043),
    (datetime(2020, 2, 18, 16, 0), 1632, 1117),
    (datetime(2020, 2, 18, 18, 0), 1766, 1219),
    (datetime(2020, 2, 18, 20, 0), 1921, 1320),
    (datetime(2020, 2, 18, 22, 0), 2049, 1378),
    (datetime(2020, 2, 19,  0, 0), 2229, 1438),
    (datetime(2020, 2, 19,  2, 0), 2388, 1484),
    (datetime(2020, 2, 19,  4, 0), 2573, 1520),
    (datetime(2020, 2, 19,  6, 0), 2698, 1551),
    (datetime(2020, 2, 19,  8, 0), 2935, 1596),
    (datetime(2020, 2, 19, 10, 0), 3094, 1629),
    (datetime(2020, 2, 19, 12, 0), 3301, 1678),
    (datetime(2020, 2, 19, 14, 0), 3550, 1781),
    (datetime(2020, 2, 19, 16, 0), 3673, 1856),
    (datetime(2020, 2, 19, 18, 0), 3818, 1967),
    (datetime(2020, 2, 19, 20, 0), 3930, 2108),
    (datetime(2020, 2, 19, 22, 0), 4045, 2251),
    (datetime(2020, 2, 20,  0, 0), 4169, 2369),
    (datetime(2020, 2, 20,  2, 0), 4278, 2438),
    (datetime(2020, 2, 20,  4, 0), 4453, 2530),
    (datetime(2020, 2, 20,  6, 0), 4614, 2607),
    (datetime(2020, 2, 20,  8, 0), 4782, 2683),
    (datetime(2020, 2, 20, 10, 0), 4959, 2785),
    (datetime(2020, 2, 20, 12, 0), 5103, 2876)
]

size = len(row_data)
t0 = row_data[0][0]


def to_hours(dt):
    return dt.days/24 + dt.seconds/3600


time = [to_hours(r[0] - t0) for r in row_data]
hits = [r[1] for r in row_data]
miss = [r[2] for r in row_data]
n    = [hits[i] + miss[i] for i in np.arange(size)]

time = range(size)
plt.plot(time, hits, 'ro', color = 'b')
plt.plot(time, miss, 'ro', color = 'g')
plt.plot(time,    n, 'bs', color = 'r')

plt.xlabel('time, hours')
plt.ylabel('count, 10^3')
plt.show()