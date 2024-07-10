import sys
import os
import unittest
import json

# Добавляем путь к task3 в sys.path, чтобы можно было импортировать json_fill_values
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'task3')))

from task3 import load_json_file, save_json_file, build_value_dict, fill_values

class TestJsonFillValues(unittest.TestCase):

    def setUp(self):
        # Создаем тестовые файлы перед каждым тестом
        with open('test_values.json', 'w') as file:
            json.dump({"values": [{"id": 1, "value": "passed"}]}, file)
        
        with open('invalid_json.txt', 'w') as file:
            file.write('{"values": [1, 2, 3')

    def tearDown(self):
        # Удаляем тестовые файлы после каждого теста
        os.remove('test_values.json')
        os.remove('invalid_json.txt')
        if os.path.exists('output.json'):
            os.remove('output.json')

    def test_load_json_file(self):
        data = load_json_file('test_values.json')
        self.assertEqual(data, {"values": [{"id": 1, "value": "passed"}]})

        with self.assertRaises(SystemExit):
            load_json_file('invalid_json.txt')

    def test_save_json_file(self):
        data = {"values": [{"id": 1, "value": "passed"}]}
        save_json_file('output.json', data)

        with open('output.json', 'r') as file:
            saved_data = json.load(file)

        self.assertEqual(data, saved_data)

    def test_build_value_dict(self):
        values = [{"id": 1, "value": "passed"}, {"id": 2, "value": "failed"}]
        value_dict = build_value_dict(values)
        self.assertEqual(value_dict, {1: "passed", 2: "failed"})

    def test_fill_values(self):
        test_structure = {
            "id": 1,
            "value": "",
            "values": [{"id": 2, "value": ""}]
        }
        value_dict = {1: "passed", 2: "failed"}
        fill_values(test_structure, value_dict)
        self.assertEqual(test_structure["value"], "passed")
        self.assertEqual(test_structure["values"][0]["value"], "failed")

    def test_invalid_file(self):
        with self.assertRaises(SystemExit):
            load_json_file('non_existent_file.txt')

if __name__ == '__main__':
    unittest.main()
