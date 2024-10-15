#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, is_prime
from src.question_b.question_b import test_config, get_fahrenheit 
from src.question_c.question_c import test_config, get_bonus_pay_amount
from src.question_d.question_d import test_config, get_assessment_value, get_tax_assessed 


class Test_Config(unittest.TestCase):
#Question A
    def test_question_a_config(self):
        self.assertEqual(True, test_config())
    def is_prim(self):
        self.assertEqual(False, is_prime(4))
        self.assertEqual(True, is_prime(5))
        self.assertEqual(True, is_prime(11))

#Question B
    def test_question_b_config(self):
        self.assertEqual(True, test_config())
    def get_fahrenheit(self):
        self.assertEqual(32, get_fahrenheit(0))
        self.assertEqual(41, get_fahrenheit(5))
        self.assertEqual(50, get_fahrenheit(10))

#Question C
    def test_question_c_config(self):
        self.assertEqual(True, test_config())
    def get_bonus_pay_amount(self):
        self.assertEqual('Invalid', get_bonus_pay_amount(-1))
        self.assertEqual(10, get_bonus_pay_amount(200))
        self.assertEqual(36, get_bonus_pay_amount(600))
        self.assertEqual(70, get_bonus_pay_amount(1000))
        self.assertEqual(120, get_bonus_pay_amount(1500))
        self.assertEqual('Invalid', get_bonus_pay_amount(2000))
    


#Question D
    def test_question_d_config(self):
        self.assertEqual(True, test_config())
    def get_assessment_value(self):
        self.assertEqual(60000, get_assessment_value(10000))
        self.assertEqual(12000, get_assessment_value(20000))
    def get_tax_assessed(self):
        self.assertEqual(43.20, get_tax_assessed(6000))
        self.assertEqual(72, get_tax_assessed(10000))
