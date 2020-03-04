import numpy as np
import matplotlib.pyplot as plt

lambda_h = 1.4/19
lambda_m = 0.7/20
lambda_r = lambda_h + lambda_m
print('Request rate: {0:.2}'.format(lambda_r))

t = np.arange(0., 40., 0.05)
H = lambda_h * t * (1 - np.exp( - lambda_h*t))
R = lambda_r * t
M = R - H

actual_t = [6.6, 11.0, 14.0, 20.0, 33.0]
actual_H = [0.3,  0.6,  0.8,  1.3,  2.2]

plt.ylim(0, 3)
plt.plot(t, H, t, M, actual_t, actual_H, 'ro')

plt.show()