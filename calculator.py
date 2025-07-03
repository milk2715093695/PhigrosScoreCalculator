import math
import time
import random
import functools
from typing import List, Tuple


def get_gcd(*coefficients: int) -> int:
    return functools.reduce(lambda x, y: math.gcd(x, y), coefficients)


def normalize(*coefficients: int) -> List[int]:
    coeff_gcd = get_gcd(*coefficients)
    return [c // coeff_gcd for c in coefficients]


def mod_inv(num: int, mod: int) -> int:
    def extended_gcd(x: int, y: int) -> Tuple[int, int, int]:
        if y == 0:
            return x, 1, 0
        gcd, x1, y1 = extended_gcd(y, x % y)
        return gcd, y1, x1 - (x // y) * y1

    gcd, x, _ = extended_gcd(num, mod)
    return x % mod if gcd == 1 else None


def get_all_k_p(A: int, S: int, gcd_123: int) -> List[int]:
    k_min = math.ceil((S - 0.5) * A / gcd_123)
    k_max = math.ceil((S + 0.5) * A / gcd_123) - 1

    all_k = [k for k in range(k_min, k_max + 1)]
    return all_k


def get_all_c(a1_pp: int, a2_pp: int, gcd_12: int, a3_p: int, k_p: int, A: int, S: int) -> List[int]:
    min_coeff, max_coeff = min(a1_pp, a2_pp), max(a1_pp, a2_pp)

    C_min = max(math.ceil((S - 900000) * A / 100000), 0)
    C_max = min(A, math.ceil(k_p / (gcd_12 * min_coeff + a3_p)))

    C_0 = mod_inv(a3_p, gcd_12) * k_p % gcd_12
    legal_C_min = C_0 + math.ceil((C_min - C_0) / gcd_12) * gcd_12

    all_C = []
    for C in range(legal_C_min, C_max + 1, gcd_12):
        k_pp = (k_p - a3_p * C) // gcd_12

        E_min = C
        E_max = math.floor((A + 1) / (C + 1) * C)
        
        if E_min * min_coeff <= k_pp <= E_max * max_coeff:
            all_C.append(C)

    return all_C


def solve(amount: int, target_score: int) -> List[Tuple[int, int, int]]:
    a1, a2, a3 = 900000, int(900000 * 0.65), 100000
    A, S = amount, target_score

    a1_p, a2_p, a3_p = normalize(a1, a2, a3)
    
    solutions = []
    for k_p in get_all_k_p(A, S, get_gcd(a1, a2, a3)):
        solutions.extend(solve_diophantine_with_three_variables(a1_p, a2_p, a3_p, k_p, A, S))

    return solutions


def solve_diophantine_with_three_variables(a1_p: int, a2_p: int, a3_p: int, k_p: int, A: int, S: int) -> List[Tuple[int, int, int]]:
    a1_pp, a2_pp = normalize(a1_p, a2_p)
    gcd_12 = get_gcd(a1_p, a2_p)
    
    solutions = []
    for C in get_all_c(a1_pp, a2_pp, gcd_12, a3_p, k_p, A, S):
        k_pp = (k_p - a3_p * C) // gcd_12
        for P, G in solve_diophantine_with_two_variables(a1_pp, a2_pp, k_pp, C, A, S):
            E = P + G
            if A >= E >= C >= math.ceil(E / (A - E + 1)):
                solutions.append((C, P, G))

    return solutions


def solve_diophantine_with_two_variables(a1_pp: int, a2_pp: int, k_pp: int, C: int, A: int, S: int) -> List[Tuple[int, int]]:
    G_min = max(0, math.ceil((a1_pp - k_pp) / (a1_pp - a2_pp)))
    G_max = min(math.floor(k_pp / a2_pp), math.floor((a1_pp * math.floor((A + 1) * C / (C + 1)) - k_pp) / (a1_pp - a2_pp)))

    G_0 = mod_inv(a2_pp, a1_pp) * k_pp % a1_pp
    legal_G_min = G_0 + math.ceil((G_min - G_0) / a1_pp) * a1_pp

    solutions = []
    for G in range(legal_G_min, G_max + 1, a1_pp):
        P = (k_pp - G * a2_pp) // a1_pp
        solutions.append((P, G))

    return solutions


if __name__ == '__main__':
    amount = int(input("输入物量: "))
    target_score = int(input("输入目标分数: "))

    start_time = time.perf_counter()
    solutions = solve(amount, target_score)
    elapsed_time = time.perf_counter() - start_time

    print(f"用时: {elapsed_time} 秒")

    if solutions:
        print(f"解的数量: {len(solutions)}")
        print(f"随机的一组解(最大连击, Perfect, Good): {random.choice(solutions)}")
    else:
        print("无解")
