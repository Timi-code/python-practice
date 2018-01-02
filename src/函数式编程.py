from functools import reduce


def f(param):
    return param * param


def add(x, y, z):
    return f(x) + z(y)


print(add(1, 2, f))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 2, 3, 4, 5]))
