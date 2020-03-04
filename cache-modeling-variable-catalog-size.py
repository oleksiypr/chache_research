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

_, rhs_H = solution_H.args

pretty_print(rhs_H.diff(t).subs(t, 0))
pretty_print(limit(rhs_H.diff(t), t, oo))
