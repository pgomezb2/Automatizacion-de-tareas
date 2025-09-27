import unittest
from src.calculator import suma, resta

class TestCalculator(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2,4), 6)
        
    def test_resta(self):
        self.assertEqual(resta(6,4), 12)
        
if __name__ == '__main__':
    unittest.main()

# from src.calculator import suma, resta

# def test_suma():
#     assert suma(2,4) == 6
    
# def test_resta():
#     assert resta(6,4) == 2
        
