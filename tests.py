import unittest
from utils import find_cheapest_path, get_data_from_path

class TestFindCheapestPath(unittest.TestCase):
    def test_basic_case(self):
        airports = [
            {'start': 'A', 'end': 'B', 'cost': 100},
            {'start': 'B', 'end': 'C', 'cost': 150},
            {'start': 'A', 'end': 'C', 'cost': 300}
        ]
        start = 'A'
        end = 'C'
        expected_output = (['A', 'B', 'C'], 250)
        self.assertEqual(find_cheapest_path(airports, start, end), expected_output)

    def test_no_path_available(self):
        airports = [
            {'start': 'A', 'end': 'B', 'cost': 100},
            {'start': 'B', 'end': 'C', 'cost': 150}
        ]
        start = 'A'
        end = 'D'
        expected_output = (None, float('inf'))
        self.assertEqual(find_cheapest_path(airports, start, end), expected_output)

    def test_multiple_paths_with_different_costs(self):
        airports = [
            {'start': 'A', 'end': 'B', 'cost': 200},
            {'start': 'A', 'end': 'C', 'cost': 100},
            {'start': 'C', 'end': 'B', 'cost': 50},
            {'start': 'B', 'end': 'D', 'cost': 100}
        ]
        start = 'A'
        end = 'D'
        expected_output = (['A', 'C', 'B', 'D'], 250)
        self.assertEqual(find_cheapest_path(airports, start, end), expected_output)

    def test_direct_path_cheaper_than_indirect(self):
        airports = [
            {'start': 'A', 'end': 'B', 'cost': 100},
            {'start': 'A', 'end': 'C', 'cost': 150},
            {'start': 'B', 'end': 'C', 'cost': 50},
            {'start': 'B', 'end': 'D', 'cost': 100}
        ]
        start = 'A'
        end = 'D'
        expected_output = (['A', 'B', 'D'], 200)
        self.assertEqual(find_cheapest_path(airports, start, end), expected_output)

    def test_cycle_in_graph(self):
        airports = [
            {'start': 'A', 'end': 'B', 'cost': 100},
            {'start': 'B', 'end': 'C', 'cost': 150},
            {'start': 'C', 'end': 'A', 'cost': 50},
            {'start': 'A', 'end': 'D', 'cost': 300}
        ]
        start = 'A'
        end = 'D'
        expected_output = (['A', 'D'], 300)
        self.assertEqual(find_cheapest_path(airports, start, end), expected_output)

    def test_same_cost_paths(self):
        airports = [
            {'start': 'A', 'end': 'B', 'cost': 100},
            {'start': 'A', 'end': 'C', 'cost': 100},
            {'start': 'B', 'end': 'D', 'cost': 200},
            {'start': 'C', 'end': 'D', 'cost': 200}
        ]
        start = 'A'
        end = 'D'
        expected_output = (['A', 'B', 'D'], 300)  # or ['A', 'C', 'D'], cost is the same
        self.assertIn(find_cheapest_path(airports, start, end), [(expected_output)])

    def test_no_airports(self):
        airports = []
        start = 'A'
        end = 'D'
        expected_output = (None, float('inf'))
        self.assertEqual(find_cheapest_path(airports, start, end), expected_output)

    def test_start_and_end_same(self):
        airports = [
            {'start': 'A', 'end': 'B', 'cost': 100},
            {'start': 'B', 'end': 'C', 'cost': 150}
        ]
        start = 'A'
        end = 'A'
        expected_output = (['A'], 0)
        self.assertEqual(find_cheapest_path(airports, start, end), expected_output)


class TestGetDataFromPath(unittest.TestCase):
    def test_get_data_from_path(self):
        path = 'data/data.json'
        expected_output = [
            {"start": "ISB", "end": "LHR", "cost": 1000},
            {"start": "LHR", "end": "NYC", "cost": 750},
            {"start": "CBS", "end": "NYC", "cost": 775},
            {"start": "ISB", "end": "CBS", "cost": 575},
            {"start": "CBS", "end": "GRC", "cost": 731},
            {"start": "NYC", "end": "GRC", "cost": 459}
        ]
        self.assertEqual(get_data_from_path(path), expected_output)

    def test_invalid_path(self):
        path = 'data/invalid.json'
        with self.assertRaises(FileNotFoundError):
            get_data_from_path(path)

    def test_empty_file(self):
        path = 'data/empty.json'
        with self.assertRaises(ValueError):
            get_data_from_path(path)

    def test_invalid_json(self):
        path = 'data/invalid_format.json'
        with self.assertRaises(ValueError):
            get_data_from_path(path)

    def test_invalid_data_format(self):
        path = 'data/invalid_data_format.json'
        with self.assertRaises(TypeError):
            get_data_from_path(path)

    def test_invalid_data_type(self):
        path = 'data/invalid_data_type.json'
        with self.assertRaises(TypeError):
            get_data_from_path(path)

    def test_missing_keys(self):
        path = 'data/missing_keys.json'
        with self.assertRaises(KeyError):
            get_data_from_path(path)
            
                     
if __name__ == '__main__':
    unittest.main(verbosity=2)