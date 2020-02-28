import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

N = 1_500_000
assumed_ttl_days = 4

t1 = datetime(2020, 2, 17, 14, 0)
t2 = datetime(2020, 2, 19, 4, 0)
dt = t2 - t1
dt_days = dt.days + dt.seconds/3600/24

N1 = 0
N2 = N
dN = N2 - N1

rate = dN/dt_days

print("Time period, days: {0:.1f}".format(dt_days))
print("Actual cache size rate 1/days: {0:.0f}".format(rate))

plt.xlabel('time, days')
plt.ylabel('cache size, 10^6')
plt.plot([0., assumed_ttl_days], [0., dN/1e6], label='assumed')
plt.plot([0.,          dt_days], [0., dN/1e6], label='actual')
plt.legend(loc="upper left")
plt.show()