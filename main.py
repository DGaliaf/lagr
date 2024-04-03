import pandas as pd
import numpy as np
import math


points = [3, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
current = 0

def F(x: np.ndarray) -> float:
    return x ** 2 - np.log(x + 5)

def Lagr(x: float) -> float:
    temp_points = list(np.linspace(0.5, 1, points[current]))
    result = 0
    for i in range(0, points[current]):
        mult = F(temp_points[i])
        for j in range(0, points[current]):
            if j != i:
                mult *= ((x - temp_points[j]) / (temp_points[i] - temp_points[j]))
        result += mult
    return result


def dF(x: float, n: int) -> float:
    if n == 3:
        return 2 - 1 / pow(x + 5, 2)
    else:
        return pow(-1, n) * math.factorial(n - 2) / pow(x + 5, n - 1)


normalize = lambda fn: max(abs(fn(x)) for x in np.linspace(0.5, 1, 1000))
abs_error = lambda fn1, fn2: max(abs(fn1(x) - fn2(x)) for x in np.linspace(0.5, 1, 1000))
rel_error = lambda fn1, fn2: ((abs_error(fn1, fn2)) / normalize(fn2)) * 100
theory_error = lambda n: (0.5 ** (n + 1)) * max(abs(dF(x, n + 1)) for x in np.linspace(0.5, 1, 1000)) / math.factorial(
    n + 1)

abs_err_mass, rel_err_mass, theory_err_mass = [], [], []

for k in range(0, len(points)):
    current = k
    abs_err, rel_err, theory_err = abs_error(Lagr, F), rel_error(Lagr, F), theory_error(points[k])

    abs_err_mass.append(abs_err)
    rel_err_mass.append(rel_err)
    theory_err_mass.append(theory_err)

output = pd.DataFrame({"N": points,
                       "Absolute Error": abs_err_mass,
                       "Relation Error": rel_err_mass,
                       "Theoretical error": theory_err_mass})

output.style.hide(axis="index")

print(output)
