import unittest
import sys
import os

# Добавляем путь к task4 в sys.path, чтобы можно было импортировать min_moves
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'task4')))

from task4 import read_numbers_from_file, min_moves_to_equal_elements

class TestMinMoves(unittest.TestCase):

    def test_min_moves(self):
        nums = [1, 2, 3]
        self.assertEqual(min_moves_to_equal_elements(nums), 2)
        
        nums = [1, 10, 2, 9]
        self.assertEqual(min_moves_to_equal_elements(nums), 16)
        
        nums = [1, 1, 1, 1]
        self.assertEqual(min_moves_to_equal_elements(nums), 0)

    def test_read_numbers_from_file(self):
        with open('test_input.txt', 'w') as file:
            file.write('1\n2\n3\n')

        nums = read_numbers_from_file('test_input.txt')
        self.assertEqual(nums, [1, 2, 3])

        with open('empty_file.txt', 'w') as file:
            pass

        with self.assertRaises(SystemExit):
            read_numbers_from_file('empty_file.txt')

        with open('invalid_numbers.txt', 'w') as file:
            file.write('1\nabc\n3\n')

        with self.assertRaises(SystemExit):
            read_numbers_from_file('invalid_numbers.txt')

    def test_invalid_file(self):
        with self.assertRaises(SystemExit):
            read_numbers_from_file('non_existent_file.txt')

if __name__ == '__main__':
    unittest.main()
