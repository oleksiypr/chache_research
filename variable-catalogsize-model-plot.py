import numpy as np
import matplotlib.pyplot as plt
from sympy import *

init_printing()

_lambda, kappa, t, K0 = symbols('lambda kappa t K_0', positive=True)

H = \
    -(_lambda * K0 / (kappa + _lambda)) \
    + _lambda / (kappa + _lambda) \
    * K0 ** (1 + _lambda / kappa) \
    * (K0 + kappa * t) ** (-_lambda / kappa) \
    + _lambda ** 2 * t / (kappa + _lambda)

pretty_print(Eq(Function('H')(t), H))

func_H = lambdify([t, _lambda, kappa, K0], H)

_lambda = 0.11
kappa = 0.06
K0 = 0.3


def calc_hits(t):
    return func_H(t, _lambda, kappa, K0)


t = np.arange(0., 40., 0.05)
plt.ylim(0, 3)

hits = calc_hits(t)
actual_t = [6.6, 11.0, 14.0, 20.0, 33.0]
actual_H = [0.3, 0.6, 0.8, 1.3, 2.2]

plt.plot(t, hits, t, 0.11 * t, '--', actual_t, actual_H, 'ro')

plt.show()
