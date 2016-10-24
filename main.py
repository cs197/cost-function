
from cost_function_definition import f, f_prime, f_double_prime


# return's a new guess using Newton's method
def newtons_method(f1, f2, guess):
    slope = f1(guess)
    curvature = f2(guess)

    if slope == 0.0:
        # already at a stationary point
        return guess

    if curvature == 0.0:
        # oh-oh, no curvature, means Newton's next guess is infinitely far away
        delta = -1.0 / slope  # the only dimensionally-correct thing to return
    else:
        # after dispensing with the special cases, finally apply Newton's method
        delta = -slope / curvature

    return guess + delta


def minimize(f0, f1, f2, guess, epsilon):
    new_guess = newtons_method(f1, f2, guess)

    while abs(new_guess - guess) >= epsilon:
        # guess again
        guess = new_guess
        new_guess = newtons_method(f1, f2, new_guess)

    print "Minimum of " + str(f0(new_guess)) + " found at " + str(new_guess)


if __name__ == "__main__":
    minimize(f, f_prime, f_double_prime, 0.0, 0.000001)
