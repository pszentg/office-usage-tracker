import unittest
from src.datapao_io.input_parser import InputParser


class TestInputParser(unittest.TestCase):

    def test_parse_input(self):
        input_file = "./resources/datapao_homework_2024.csv"
        parsed_data = InputParser.parse_input(input_file)
        self.assertTrue(len(parsed_data) > 0)
        self.assertIn("user_id", parsed_data[0])
        self.assertIn("event_type", parsed_data[0])
        self.assertIn("event_time", parsed_data[0])

    def test_input_does_not_exist(self):
        input_file = "./non-existent-path.csv"
        with self.assertRaises(OSError) as context:
            InputParser.parse_input(input_file)

        self.assertTrue("File does not exist!" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
