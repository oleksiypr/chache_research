from sympy import *
from sympy.simplify.simplify import *

init_printing()

K = symbols('K', positive = True)
N, t = symbols('N t', positive = True)
S = Function('S')(N)
H = Function('H')(N)

diff_eq_S = Eq(S.diff(N), 1 - S/K)
pretty_print(diff_eq_S)

solution_S = dsolve(diff_eq_S, S)
pretty_print(solution_S)

C1 = solve(solution_S.subs({S: 0, N: 0}), 'C1')[0]
solution_S = factor_sum(solution_S.subs('C1', C1))
pretty_print(solution_S)

diff_eq_H = Eq(H.diff(N), S/K)
pretty_print(diff_eq_H)

diff_eq_H = diff_eq_H.subs(S, solution_S.args[1])
pretty_print(diff_eq_H)

solution_H = dsolve(diff_eq_H, H)
pretty_print(solution_H)

C1 = solve(solution_H.subs({H: 0, N: 0}), 'C1')[0]
solution_H = solution_H.subs('C1', C1)
pretty_print(solution_H)

lhs_H, rhs_H = solution_H.args
pretty_print(solution_H.subs(N, 0))

der_H = Derivative(H, N)
eq_h = Eq(der_H, rhs_H.diff(N))
pretty_print(eq_h)
pretty_print(eq_h.subs(N, 0))

pretty_print(
    Eq(
        Limit(der_H, N, oo),
        limit(rhs_H.diff(N), N, oo)))

pretty_print(
    Eq(
        Limit(H/N, N, oo),
        limit(rhs_H/N, N, oo)))


