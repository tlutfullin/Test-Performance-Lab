import unittest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'task2')))

from task2 import read_circle_data, read_points, point_position

class TestPointCirclePosition(unittest.TestCase):

    def setUp(self):
        # Создаем тестовые файлы перед каждым тестом
        with open('circle_data.txt', 'w') as file:
            file.write('0 0\n5\n')

        with open('invalid_circle_data.txt', 'w') as file:
            file.write('0 0\nabc\n')

        with open('points_data.txt', 'w') as file:
            file.write('0 0\n3 4\n6 6\n')

        with open('invalid_points.txt', 'w') as file:
            file.write('0 0\nabc def\n')

    def tearDown(self):
        # Удаляем тестовые файлы после каждого теста
        os.remove('circle_data.txt')
        os.remove('invalid_circle_data.txt')
        os.remove('points_data.txt')
        os.remove('invalid_points.txt')

    def test_point_position(self):
        circle_center = (0, 0)
        radius = 5

        self.assertEqual(point_position(circle_center, radius, (3, 4)), 0)
        self.assertEqual(point_position(circle_center, radius, (0, 0)), 1)
        self.assertEqual(point_position(circle_center, radius, (6, 6)), 2)

    def test_read_circle_data(self):
        circle_center, radius = read_circle_data('circle_data.txt')
        self.assertEqual(circle_center, (0, 0))
        self.assertEqual(radius, 5)

        with self.assertRaises(SystemExit):
            read_circle_data('invalid_circle_data.txt')

    def test_read_points(self):
        points = read_points('points_data.txt')
        self.assertEqual(points, [(0, 0), (3, 4), (6, 6)])

        with self.assertRaises(SystemExit):
            read_points('invalid_points.txt')

    def test_invalid_file(self):
        with self.assertRaises(SystemExit):
            read_circle_data('non_existent_file.txt')
        with self.assertRaises(SystemExit):
            read_points('non_existent_file.txt')

if __name__ == '__main__':
    unittest.main()
