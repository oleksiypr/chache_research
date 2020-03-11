from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from sympy.simplify.simplify import *

_lambda, kappa, t, K0 = symbols('lambda kappa t K_0', positive=True)

"""
lambda_h_start = 0.7327, H_star_0 = -0.187
lambda_s_start = 0.3797, S_star_0 =  0.189
lambda_n       = 1.109,  n_0      =  0.019
"""

lambda_h_start = 0.749
lambda_s_start = 0.360
print("lambda_h_start + lambda_s_start: lambda = {0:.4}".format(lambda_h_start + lambda_s_start))

lmbd = 1.109
lambda_n = lmbd

H_star_0 = 0.25
S_star_0 = 0.189

eq_h_star = Eq(lambda_h_start, lambda_n**2 / (kappa + lambda_n))
h_star_kappa = solve(eq_h_star, kappa)[0]
print("From lambda_h_star: kappa = {0:.4}".format(h_star_kappa))

eq_s_star = Eq(lambda_s_start, lambda_n * kappa / (kappa + lambda_n))
s_star_kappa = solve(eq_s_star, kappa)[0]
print("From lambda_s_star: kappa = {0:.4}".format(s_star_kappa))

eq_K0_H0 = Eq(H_star_0, K0 * lambda_n / (kappa + lambda_n)).subs(kappa, h_star_kappa)
K0_H0_h_star_K0 = solve(eq_K0_H0, K0)[0]
print("From H_0_star and h_star_kappa: K0 = {0:.3}".format(K0_H0_h_star_K0))

eq_K0_H0 = Eq(H_star_0, K0 * lambda_n / (kappa + lambda_n)).subs(kappa, s_star_kappa)
K0_H0_s_star_kappa = solve(eq_K0_H0, K0)[0]
print("From H_0_star and s_star_kappa: K0 = {0:.3}".format(K0_H0_s_star_kappa))

# date, hits * 1e3, mis * 1e3
raw_data = [
    (datetime(2020, 2, 17, 15,  9),   0,    1),
    (datetime(2020, 2, 17, 15, 18),   1,   18),
    (datetime(2020, 2, 17, 15, 30),   4,   42),
    (datetime(2020, 2, 17, 16,  0),   8,   72),
    (datetime(2020, 2, 17, 16, 30),  17,  119),
    (datetime(2020, 2, 17, 17,  0),  30,  155),
    (datetime(2020, 2, 17, 17, 30),  48,  195),
    (datetime(2020, 2, 17, 18,  0),  69,  235),
    (datetime(2020, 2, 17, 19,  0), 123,  315),
    (datetime(2020, 2, 17, 20,  0), 184,  389),
    (datetime(2020, 2, 17, 21,  0), 260,  451),
    (datetime(2020, 2, 17, 22,  0), 314,  484),
    (datetime(2020, 2, 17, 22, 40), 392,  530),
    (datetime(2020, 2, 17, 23, 52), 412,  540),
    (datetime(2020, 2, 17, 23, 55), 455,  558),
    (datetime(2020, 2, 18,  0, 30), 535,  593),
    (datetime(2020, 2, 18,  1, 20), 566,  616),
    (datetime(2020, 2, 18,  2, 10), 646,  644),
    (datetime(2020, 2, 18,  3, 20), 736,  680),
    (datetime(2020, 2, 18,  4, 0),  774,  711),
    (datetime(2020, 2, 18,  5, 0),  817,  731),
    (datetime(2020, 2, 18,  6, 0),  878,  757),
    (datetime(2020, 2, 18,  8, 0), 1036,  826),
    (datetime(2020, 2, 18, 10, 0), 1231,  901),
    (datetime(2020, 2, 18, 12, 0), 1375,  969),
    (datetime(2020, 2, 18, 14, 0), 1490, 1043),
    (datetime(2020, 2, 18, 16, 0), 1632, 1117),
    (datetime(2020, 2, 18, 18, 0), 1766, 1219),
    (datetime(2020, 2, 18, 19, 0), 1838, 1273),
    (datetime(2020, 2, 18, 20, 0), 1921, 1320),
    (datetime(2020, 2, 18, 22, 0), 2049, 1378),
    (datetime(2020, 2, 19,  0, 0), 2229, 1438),
    (datetime(2020, 2, 19,  1, 0), 2294, 1457),
    (datetime(2020, 2, 19,  2, 0), 2388, 1484)]


def to_hours(dt):
    return dt.days*24 + dt.seconds/3600


lambda_n, kappa, K0 = symbols('lambda kappa K_0', positive=True)

H = -(lambda_n * K0 / (kappa + lambda_n)) \
    + lambda_n / (kappa + lambda_n) \
    * K0 ** (1 + lambda_n / kappa) \
    * (K0 + kappa * t) ** (-lambda_n / kappa) \
    + lambda_n ** 2 * t / (kappa + lambda_n)

S = - (lambda_n / (kappa + lambda_n)) \
    * K0 ** (1 + lambda_n / kappa) \
    * (K0 + kappa*t) ** (-lambda_n / kappa) \
    + (lambda_n / (kappa + lambda_n)) * (K0 + kappa * t)


func_H = lambdify([t, lambda_n, kappa, K0], H)
func_S = lambdify([t, lambda_n, kappa, K0], S)


lambda_n = lmbd
kappa    = h_star_kappa
K0       = K0_H0_h_star_K0

def calc_hits(t):
    return func_H(t, lambda_n, kappa, K0)


def calc_miss(t):
    return func_S(t, lambda_n, kappa, K0)


t0 = datetime(2020, 2, 17, 15, 8, 30)


time = [to_hours(r[0] - t0) / 10.0 for r in raw_data]
hits_data = [r[1] / 1000.0 for r in raw_data]
miss_data = [r[2] / 1000.0 for r in raw_data]

t = np.arange(0., 3., 0.05)
hits = calc_hits(t)
miss = calc_miss(t)

plt.plot(t, hits)
plt.plot(t, miss)
plt.plot(t, hits + miss)

plt.plot(time, hits_data, 'ro', color ='b')
plt.plot(time, miss_data, 'ro', color ='g')

plt.xlim(left   =  0.0, right = 4)
plt.ylim(bottom = -0.5, top   = 3)

plt.show()