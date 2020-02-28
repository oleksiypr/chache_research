from sympy import *

init_printing()

t = symbols('t')
P = Function('P')(t)
H = Function('H')(t)
lambda_h = symbols('lambda_h', positive=True)

Hits_count = lambda_h * t * (1 - exp(-lambda_h * t))
hit_function = Hits_count.diff(t)
der_H = Derivative(H, t)

eq_H = Eq(H, Hits_count)
eq_h = Eq(der_H, hit_function)

pretty_print(eq_H)
pretty_print(eq_h)

f = solve(eq_H, lambda_h * (1 - exp(-lambda_h * t)))[0]
pretty_print(Eq(symbols('f'), f))

hit_function = hit_function.subs(lambda_h * (1 - exp(-lambda_h * t)), f)
eq_h = Eq(der_H, hit_function)
pretty_print(eq_h)

f = solve(eq_H, exp(-lambda_h*t))[0]
eq_exp_lmbd_t = Eq(exp(-lambda_h*t),  f)
pretty_print(eq_exp_lmbd_t)

lhs, rhs = eq_exp_lmbd_t.args
f = expand(rhs * lambda_h**2 * t)
eq_exp_lmbd_t = Eq(lhs * lambda_h**2 * t, f)
pretty_print(eq_exp_lmbd_t)

hit_function = hit_function.subs(lambda_h**2 * t * exp(-lambda_h * t), f)
eq_h = Eq(der_H, hit_function)
pretty_print(eq_h)




