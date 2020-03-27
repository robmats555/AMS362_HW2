import random
import math
import numpy as np
import matplotlib.pyplot as plt

interpol_vals = [1, 9, 18, 27, 36, 45]
degree = 5


def normal_dist(mean, sd):
    u1 = random.uniform(0, 1)
    u2 = random.uniform(0, 1)
    g1 = math.sqrt(-2 * np.log(u1)) * math.cos(2*math.pi*u2)
    g2 = math.sqrt(-2 * np.log(u1)) * math.sin(2*math.pi*u2)
    z1 = mean + (g1 * sd)
    z2 = mean + (g2 * sd)

    if random.uniform(0, 1) < 0.5:
        return z1
    else:
        return z2


def generate_cases():
    cases = [10]
    for i in range(44):
        z = normal_dist(0.18, 0.08)
        cases.append(math.ceil((cases[i] * (1 + z))))
    for i in range(44, 89):
        z = normal_dist(-0.24, 0.04)
        cases.append(math.ceil((cases[i] * (1 + z))))
    return cases


def plot_cases(cases):
    t = np.arange(0, 90, 1)
    plt.plot(t, cases, 'ro')
    plt.grid(True)


def power_row(power, val):
    result = []
    for p in range(power+1):
        result.append(val**p)
    return result


def gen_interpol_coef(cases):
    X = []
    for val in interpol_vals:
        X.append(power_row(degree, val))

    y = [el for ind, el in enumerate(cases) if ind + 1 in interpol_vals]

    X = np.array(X)
    y = np.array(y)

    a = np.linalg.solve(X, y)
    return a


def plot_interpolation(cases):
    t = np.arange(1, 46, 1)
    y = []

    a = np.array(gen_interpol_coef(cases))
    for i in t:
        pt = np.array(power_row(degree, i)).dot(a)
        y.append(pt)

    plt.plot(t, y)


def summation(*args):
    result = args[0].copy()
    for i, arg in enumerate(args):
        if i != 0:
            result *= arg
    return sum(result)


def gen_fit_coef(cases):
    t = np.arange(46, 91, 1)
    log_cases = np.log(cases)

    lny = summation(log_cases)
    xx = summation(t, t)
    x = summation(t)
    xlny = summation(log_cases, t)

    a = (lny*xx - x*xlny)/(45*xx - x*x)
    b = (45*xlny - x*lny)/(45*xx - x*x)

    return math.exp(a), b


def plot_fitting(cases):
    a, b = gen_fit_coef(cases)

    t = np.arange(46, 91, 1)
    points = []
    for el in t:
        points.append(a * math.exp(b*el))

    plt.plot(t, points)


def main():
    cases = generate_cases()
    plot_cases(cases)
    plot_interpolation(cases[:45])
    plot_fitting(cases[45:])
    plt.show()


main()
