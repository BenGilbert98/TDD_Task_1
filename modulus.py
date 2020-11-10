class Modulus:

    def modulus(self, num1, num2):
        return num1 % num2

    def is_positive(self, num1, num2):
        if num1 and num2 > 0:
            return True
        if num1 or num2 < 0:
            return False