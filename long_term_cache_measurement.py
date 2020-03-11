from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from sympy import pretty_print, init_printing

init_printing()

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
    (datetime(2020, 2, 19,  2, 0), 2388, 1484)]

''' below cache size exeeds

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
'''

size = len(row_data)
t0 = datetime(2020, 2, 17, 15, 18)

def to_hours(dt):
    return dt.days*24 + dt.seconds/3600


time = [to_hours(r[0] - t0)/10.0 for r in row_data]
hits = [r[1]/1000.0 for r in row_data]
miss = [r[2]/1000.0 for r in row_data]
n    = [hits[i] + miss[i] for i in np.arange(size)]

A = np.vstack([time, np.ones(len(hits))]).T
lambda_h_start_0, H_star_0 = np.linalg.lstsq(A, hits, rcond=None)[0]
print(lambda_h_start_0)
print(H_star_0)

A = np.vstack([time, np.ones(len(hits))]).T
lambda_s_start_0, S_star_0 = np.linalg.lstsq(A, miss, rcond=None)[0]
print(lambda_s_start_0)
print(S_star_0)

A = np.vstack([time, np.ones(len(hits))]).T
lambda_n, n_0 = np.linalg.lstsq(A, n, rcond=None)[0]
print(lambda_n)
print(n_0)

time_origin = [0.0] + time

plt.plot(time, hits, 'ro', color = 'b')
plt.plot(time, miss, 'ro', color = 'g')
plt.plot(time,    n, 'bs', color = 'r')

plt.plot(time_origin, [lambda_h_start_0 * t + H_star_0 for t in time_origin])
plt.plot(time_origin, [lambda_s_start_0 * t + S_star_0 for t in time_origin])
plt.plot(time_origin, [lambda_n * t + n_0 for t in time_origin])

plt.xlim(left   = 0.0)
plt.ylim(bottom = 0.0)

plt.xlabel('time, 10 hours')
plt.ylabel('count, 10^6')
plt.show()