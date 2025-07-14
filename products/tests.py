from django.test import TestCase
from .calculator import Calculator
# Create your tests here.
class CalculatorTest(TestCase):
    
    def setUp(self):
        self.calculator=Calculator()
    
    def test_add(self):
        self.assertEqual(self.calculator.add(12,2),14)
        self.assertEqual(self.calculator.add(2,2),4)
        self.assertEqual(self.calculator.add(4,4),8)
        self.assertEqual(self.calculator.add(2,3),5)

    def test_isEven(self):
        self.assertTrue(self.calculator.is_even(4))
        self.assertTrue(self.calculator.is_even(6))
        self.assertTrue(self.calculator.is_even(14))
        self.assertTrue(self.calculator.is_even(60))

        self.assertFalse(self.calculator.is_even(29))
        self.assertFalse(self.calculator.is_even(63))
        self.assertFalse(self.calculator.is_even(1))
        self.assertFalse(self.calculator.is_even(9))

        with self.assertRaises(TypeError):
            self.calculator.is_even("")



