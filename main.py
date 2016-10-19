
from cost_function_definition import f, f_prime, f_double_prime


def minimize(f0, f1, f2, guess, epsilon):
    print str(f0(guess)) + " is minimized at " + str(guess)


minimize(f, f_prime, f_double_prime, 0, 0.000001)
