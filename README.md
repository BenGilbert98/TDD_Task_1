# Task Definition
- create a test to check that the remainder of two numbers is 0
- if true pass the test 
- if false fail the test
- create a class and method to write code to pass the test
- create a method to find if the numbers used are positive



## Task Solution
- The first thing to do is create a test file and a file ```test_<file_name>``` and ```<file_name>``` respectively.
- The next step is to create the test which will be used to verify the function is working
```
from modulus import Modulus
import unittest
import pytest


class Modulus_test(unittest.TestCase):
    mod = Modulus()
    # test_modulus function defined
    def test_modulus(self):
        self.assertEqual(self.mod.modulus(2, 2), 0)

    # test_positive function defined
    def test_positive(self):
        self.assertEqual(self.mod.is_positive(2, 2), True)
```
- A test is run using ```python -m unittest discover -v``` inside the terminal (Fail Expected)
- Then, the code is built inside the <file_name> file to satisfy the test
```
# Modulus class is defined
class Modulus:

    def modulus(self, num1, num2):
        return num1 % num2

    def is_positive(self, num1, num2):
        if num1 and num2 > 0:
            return True
        if num1 or num2 < 0:
            return False
```

- The test is rerun using ```python -m unittest discover -v``` inside the terminal (Success Expected)