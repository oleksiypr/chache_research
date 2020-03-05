import numpy as np
import matplotlib.pyplot as plt
from sympy import *

init_printing()

_lambda, kappa, t, K0 = symbols('lambda kappa t K_0', positive=True)

H = -(_lambda * K0 / (kappa + _lambda)) \
    + _lambda/(kappa + _lambda)\
        * K0**(1 + _lambda/kappa)\
        * (K0 + kappa * t)**(-_lambda / kappa) \
    + _lambda ** 2 * t / (kappa + _lambda)

S = - (_lambda/(kappa + _lambda)) \
        * K0**(1 + _lambda/kappa) \
        * (K0 + kappa*t)**(-_lambda/kappa) \
    + (_lambda/(kappa + _lambda)) * (K0 + kappa*t)

pretty_print(Eq(Function('H')(t), H))
pretty_print(Eq(Function('S')(t), S))

func_H = lambdify([t, _lambda, kappa, K0], H)
func_S = lambdify([t, _lambda, kappa, K0], S)

_lambda = 1
kappa = 0.1
K0 = 0.7


def calc_hits(t):
    return func_H(t, _lambda, kappa, K0)


def calc_miss(t):
    return func_S(t, _lambda, kappa, K0)


t = np.arange(0., 3., 0.05)
hits = calc_hits(t)
miss = calc_miss(t)

plt.plot(t, hits, color = 'b')
plt.plot(t, miss, color = 'g')
plt.plot(t, hits + miss, color = 'r')
plt.show()
