import unittest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'task1')))

from task1 import circular_array_path


class TestCircularArrayPath(unittest.TestCase):
    def test_valid_cases(self):
        self.assertEqual(circular_array_path(5, 2), "13524")
        self.assertEqual(circular_array_path(7, 3), "1462573")
        self.assertEqual(circular_array_path(3, 1), "123")
        self.assertEqual(circular_array_path(4, 4), "14")
        self.assertEqual(circular_array_path(6, 5), "162534")

    def test_invalid_cases(self):
        with self.assertRaises(ValueError):
            circular_array_path(-1, 3)
        with self.assertRaises(ValueError):
            circular_array_path(0, 2)
        with self.assertRaises(ValueError):
            circular_array_path(3, -2)
        with self.assertRaises(ValueError):
            circular_array_path(4, 0)
        
    def test_edge_cases(self):
        self.assertEqual(circular_array_path(1, 1), "1")
        self.assertEqual(circular_array_path(1, 100), "1")
        self.assertEqual(circular_array_path(10, 10), "10")

if __name__ == '__main__':
    unittest.main()
