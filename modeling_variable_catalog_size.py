from sympy import *
from sympy.simplify.simplify import *

init_printing()

_lambda, kappa, t, K0 = symbols('lambda kappa t K_0', positive=True)
S = Function('S')(t)
H = Function('H')(t)

K = kappa * t + K0
diff_eq_S = Eq(S.diff(t), _lambda * (1 - S/K))
diff_eq_H = Eq(H.diff(t), _lambda * S/K)

pretty_print(diff_eq_S)
pretty_print(diff_eq_H)

solution_S = simplify(dsolve(diff_eq_S, S))

C1 = solve(solution_S.subs({S: 0, t: 0}), 'C1')[0]

solution_S = simplify(solution_S.subs('C1', C1))
pretty_print(solution_S)

_, rhs_S = solution_S.args

diff_eq_H = diff_eq_H.subs(S, rhs_S)
pretty_print(diff_eq_H)
solution_H = dsolve(diff_eq_H, H)
pretty_print(solution_H)

C1 = solve(solution_H.subs({H: 0, t: 0}), 'C1')[0]
solution_H = product_simplify(solution_H.subs('C1', C1))
pretty_print(solution_H)

_, rhs_H = solution_H.args

der_H = Derivative(H, t)
pretty_print(simplify(Eq(der_H, rhs_H.diff(t)).subs(t, 0)))
pretty_print(
    Eq(
        Limit(der_H, t, oo),
        limit(rhs_H.diff(t), t, oo)))

pretty_print(
    Eq(
        Limit(H/t, t, oo),
        limit(rhs_H/t, t, oo)))

pretty_print(simplify(solution_H.subs(t, 0)))

N = Function('N')(t)
eq_N = Eq(N, S + H)
pretty_print(eq_N)
pretty_print(simplify(eq_N.subs({
    S: rhs_S,
    H: rhs_H
})))

rhs_another_view_H = \
    -(_lambda * K0 / (kappa + _lambda)) \
    + _lambda/(kappa + _lambda)\
        * K0**(1 + _lambda/kappa)\
        * (K0 + kappa * t)**(-_lambda / kappa) \
    + _lambda ** 2 * t / (kappa + _lambda)

assert rhs_H - rhs_another_view_H

rhs_another_view_S = \
    - (_lambda/(kappa + _lambda)) \
        * K0**(1 + _lambda/kappa) \
        * (K0 + kappa*t)**(-_lambda/kappa) \
    + (_lambda/(kappa + _lambda)) * (K0 + kappa*t)

assert rhs_S - rhs_another_view_S

pretty_print(Eq(H, rhs_another_view_H))
pretty_print(Eq(S, rhs_another_view_S))
