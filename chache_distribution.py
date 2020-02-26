from sympy import *

init_printing()

t = symbols('t')
P = Function('P')(t)
H = Function('H')(t)
lambda_h = symbols('lambda_h', positive=True)

Hits_count = lambda_h * t * (1 - exp(-lambda_h * t))
eq_H = Eq(H, Hits_count)
pretty_print(eq_H)
pretty_print(eq_H.subs(t, 0))

hit_function = Hits_count.diff(t)
der_H = Derivative(H, t)
eq_h = Eq(der_H, hit_function)
pretty_print(eq_h)
pretty_print(eq_h.subs(t, 0))

pretty_print(
    Eq(
        Limit(der_H, t, oo),
        limit(hit_function, t, oo)))

pretty_print(
    Eq(
        Limit(H/t, t, oo),
        limit(Hits_count/t, t, oo)))

pretty_print(eq_H.subs(1 - exp(-lambda_h * t), P))
