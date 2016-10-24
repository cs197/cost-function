
import unittest

from main import newtons_method


def f0(x):
    return 0.5 * x * x


def f1(x):
    return x


# noinspection PyUnusedLocal
def f2(x):
    return 1.0


class TestNewtonsMethod(unittest.TestCase):

    def test_upper(self):
        guess = -1.0
        new_guess = newtons_method(f1, f2, guess)
        expected_new_guess = 0.0
        self.assertEqual(new_guess, expected_new_guess)
