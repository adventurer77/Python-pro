import math 
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")

file_handler = logging.FileHandler("fraction_05.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

class ErrorEnteringPrice(Exception):

    def __init__(self, message):

        self.message = message

    def __str__(self):
        return f"{self.message}."

class ProperFraction:
    def __init__(self, numerator, denominator):

        if not isinstance(numerator,int):
            logger.error("Numerator must be a number.")
            raise TypeError("Numerator must be a number.")
        if numerator <= 0:
            logger.error("The numerator cannot be less than or equal to zero")
            raise ErrorEnteringPrice("The numerator cannot be less than or equal to zero") 
        if not isinstance(denominator,int):
            logger.error("Denominator must be a number.")
            raise TypeError("Denominator must be a number.")
        if denominator <= 0:
            logger.error("The denominator cannot be less than or equal to zero")
            raise ErrorEnteringPrice("The denominator cannot be less than or equal to zero")


        self.numerator = numerator
        self.denominator = denominator

    def __sub__(self, other):
        common_denominator_sub = self.denominator * other.denominator
        new_numerator_self_sub = self.numerator * other.denominator
        new_numerator_other_sub = other.numerator * self.denominator
        result_numerator_sub = new_numerator_self_sub - new_numerator_other_sub

        return ProperFraction(result_numerator_sub, common_denominator_sub)
    
    def __add__(self,other):
        common_denominator_add = self.denominator * other.denominator
        new_numerator_self_add = self.numerator * other.denominator
        new_numerator_other_add = other.numerator * self.denominator
        result_numerator_add = new_numerator_self_add + new_numerator_other_add

        return ProperFraction(result_numerator_add, common_denominator_add)
    
    def __mul__(self,other):
        
        common_numerator_mul = self.numerator * other.numerator
        common_denominator_mul = self.denominator * other.denominator

        return  ProperFraction(common_numerator_mul, common_denominator_mul)
    
    def __lt__(self, other):

        common_denominator = self.denominator * other.denominator
        new_numerator_self = self.numerator * other.denominator
        new_numerator_other = other.numerator * self.denominator

        return new_numerator_self > new_numerator_other

    def __eq__(self, other):
        
        common_denominator = self.denominator * other.denominator
        new_numerator_self = self.numerator * other.denominator
        new_numerator_other = other.numerator * self.denominator

        return new_numerator_self == new_numerator_other


    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

try:
    fraction1 = ProperFraction(6, 11)
    fraction2 = ProperFraction(3, 7)

    result = fraction1 - fraction2
    result.simplify()
    print(f"Result: {result.numerator}/{result.denominator}")


    fraction3 = ProperFraction(3, 7)
    fraction4 = ProperFraction(6, 11)

    result2 = fraction3 + fraction4
    result2.simplify()

    print(f"Result: {result2.numerator}/{result2.denominator}")


    fraction5 = ProperFraction(3, 7)
    fraction6 = ProperFraction(2, 5)

    result3 = fraction5 * fraction6
    result3.simplify()

    print(f"Result: {result3.numerator}/{result3.denominator}")

    fraction5 = ProperFraction(8, 9)
    fraction6 = ProperFraction(5, 6)

    if fraction5 > fraction6:
        print(f"{fraction5.numerator}/{fraction5.denominator} greater than {fraction6.numerator}/{fraction6.denominator}.")
    elif fraction1 < fraction2:
        print(f"{fraction6.numerator}/{fraction6.denominator} greater than {fraction5.numerator}/{fraction5.denominator}.")
    else:
        print(f"{fraction5.numerator}/{fraction5.denominator} equal {fraction6.numerator}/{fraction6.denominator}.")

except Exception as e:
    print(e)