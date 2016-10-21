

def f(x):
    return (x - 1) * (x - 3) * (x - 5) * (x - 7)


def f_prime(x):
    return (x - 3) * (x - 5) * (x - 7) + \
           (x - 1) * (x - 5) * (x - 7) + \
           (x - 1) * (x - 3) * (x - 7) + \
           (x - 1) * (x - 3) * (x - 5)


def f_double_prime(x):
    return 2 * (x - 5) * (x - 7) + \
           2 * (x - 3) * (x - 7) + \
           2 * (x - 1) * (x - 7) + \
           2 * (x - 3) * (x - 5) + \
           2 * (x - 1) * (x - 5) + \
           2 * (x - 1) * (x - 3)
