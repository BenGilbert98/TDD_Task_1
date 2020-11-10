from modulus import Modulus
import unittest
import pytest


class Modulus_test(unittest.TestCase):
    mod = Modulus()

    def test_modulus(self):
        self.assertEqual(self.mod.modulus(2, 2), 0)

    # test_positive function defined
    def test_positive(self):
        self.assertEqual(self.mod.is_positive(2, 2), True)
