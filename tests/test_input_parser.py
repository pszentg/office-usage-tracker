import unittest
from src.datapao_io.input_parser import InputParser


class TestInputParser(unittest.TestCase):
    def setUp(self):
        self.input_file = "./resources/datapao_homework_2024.csv"

    def test_parse_input(self):
        parsed_data = InputParser.parse_input(self.input_file)
        self.assertTrue(len(parsed_data) > 0)
        self.assertIn("user_id", parsed_data[0])
        self.assertIn("event_type", parsed_data[0])
        self.assertIn("event_time", parsed_data[0])


if __name__ == "__main__":
    unittest.main()
