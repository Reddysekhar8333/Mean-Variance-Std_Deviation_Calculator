import unittest
from mean_var_std import calculate

class TestCalculateFunction(unittest.TestCase):
    
    def test_calculate_valid_input(self):
        input_list = [0,1,2,3,4,5,6,7,8]
        result = calculate(input_list)
        
        # Test mean
        self.assertEqual(result['mean'], [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0])
        
        # Test variance
        self.assertEqual(result['variance'], [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667])
        
        # Test max
        self.assertEqual(result['max'], [[6, 7, 8], [2, 5, 8], 8])
        
        # Test min
        self.assertEqual(result['min'], [[0, 1, 2], [0, 3, 6], 0])
        
        # Test sum
        self.assertEqual(result['sum'], [[9, 12, 15], [3, 12, 21], 36])
    
    def test_calculate_invalid_input(self):
        # Test with less than 9 elements
        with self.assertRaises(ValueError) as context:
            calculate([1,2,3,4,5,6,7,8])
        self.assertEqual(str(context.exception), "List must contain nine numbers.")
        
        # Test with more than 9 elements
        with self.assertRaises(ValueError) as context:
            calculate([1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(str(context.exception), "List must contain nine numbers.")

if __name__ == '__main__':
    unittest.main()