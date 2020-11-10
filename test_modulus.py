from modulus import Modulus
import unittest


class Modulus_test(unittest.TestCase):
    mod = Modulus()

    def test_modulus(self):
        self.assertEqual(self.mod.modulus(4, 2), 0)
        # checks to see if there is no remainder when 4 is divided by 2

    # test_positive function defined
    def test_positive(self):
        self.assertEqual(self.mod.is_positive(2, 4), True)
        # checks to see if 2 and 4 are positive
