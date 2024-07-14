import unittest
import os
from config import Config
from main import main, FilterType


class TestMainIntegration(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        Config.OUTPUT_PATH = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "output/tests"
        )
        # Set up paths and configurations
        self.resources_path = "resources"
        self.input_file = os.path.join(self.resources_path, "tests/test_input.csv")

        if not os.path.exists(Config.OUTPUT_PATH):
            os.makedirs(Config.OUTPUT_PATH)

        # Ensure the input file exists for testing
        if not os.path.exists(self.input_file):
            raise FileNotFoundError("Input file for tests not found!")

    def test_main_year_filter(self):
        Config.OUTPUT_PATH = os.path.join(Config.OUTPUT_PATH, "year")
        main(input_path=self.input_file, filter_type=FilterType.YEAR, filter_value=2024)
        first_output_path = os.path.join(Config.OUTPUT_PATH, "first.csv")
        second_output_path = os.path.join(Config.OUTPUT_PATH, "second.csv")

        # Check if output files are created
        self.assertTrue(
            os.path.exists(first_output_path), "First output file not created!"
        )
        self.assertTrue(
            os.path.exists(second_output_path), "Second output file not created!"
        )

        # Optionally, you can read the files and assert on their content
        with open(first_output_path, "r") as file:
            first_content = file.read()
            self.assertIn("user_id", first_content)

        with open(second_output_path, "r") as file:
            second_content = file.read()
            self.assertIn("user_id", second_content)

    def test_main_custom_filter(self):

        Config.OUTPUT_PATH = os.path.join(Config.OUTPUT_PATH, "custom")
        main(
            input_path=self.input_file,
            filter_type=FilterType.CUSTOM,
            filter_value="2024-01-01:2024-06-30",
        )
        first_output_path = os.path.join(Config.OUTPUT_PATH, "first.csv")
        second_output_path = os.path.join(Config.OUTPUT_PATH, "second.csv")

        self.assertTrue(
            os.path.exists(first_output_path), "First output file not created!"
        )
        self.assertTrue(
            os.path.exists(second_output_path), "Second output file not created!"
        )

        expected_first_output = (
            "user_id,time,days,average_per_day,rank\n"
            "d22c03ba-00f7-4473-bc9d-61136643994f,9.0,1,9.000,1\n"
            "abce78a1-f8e6-4e9b-aafe-9786846e089e,9.0,1,9.000,2\n"
            "p3b4e81f-79de-4937-ba87-aec8e7e731af,9.0,1,9.000,3\n"
            "a8c60645-aef4-4b4e-aefb-65e242536c2f,9.0,1,9.000,4\n"
            "a59f9f64-2937-40e6-bc28-e43fbab63a65,9.0,1,9.000,5\n"
        )
        with open(first_output_path, "r") as file:
            first_content = file.read()
            self.assertEqual(first_content.strip(), expected_first_output.strip())

        expected_second_output = (
            "user_id,session_length\n" "d22c03ba-00f7-4473-bc9d-61136643994f,9H:0m:0s\n"
        )
        with open(second_output_path, "r") as file:
            second_content = file.read()
            self.assertEqual(second_content.strip(), expected_second_output.strip())

    def test_main_month_filter(self):
        Config.OUTPUT_PATH = os.path.join(Config.OUTPUT_PATH, "month")
        main(
            input_path=self.input_file,
            filter_type=FilterType.MONTH,
            filter_value="July",
        )
        first_output_path = os.path.join(Config.OUTPUT_PATH, "first.csv")
        second_output_path = os.path.join(Config.OUTPUT_PATH, "second.csv")

        # Check if output files are created
        self.assertTrue(
            os.path.exists(first_output_path), "First output file not created!"
        )
        self.assertTrue(
            os.path.exists(second_output_path), "Second output file not created!"
        )

        # Optionally, you can read the files and assert on their content
        with open(first_output_path, "r") as file:
            first_content = file.read()
            self.assertIn("user_id", first_content)

        with open(second_output_path, "r") as file:
            second_content = file.read()
            self.assertIn("user_id", second_content)

    def test_main_week_filter(self):
        Config.OUTPUT_PATH = os.path.join(Config.OUTPUT_PATH, "week")
        main(input_path=self.input_file, filter_type=FilterType.WEEK, filter_value=None)
        first_output_path = os.path.join(Config.OUTPUT_PATH, "first.csv")
        second_output_path = os.path.join(Config.OUTPUT_PATH, "second.csv")

        # Check if output files are created
        self.assertTrue(
            os.path.exists(first_output_path), "First output file not created!"
        )
        self.assertTrue(
            os.path.exists(second_output_path), "Second output file not created!"
        )

        # Optionally, you can read the files and assert on their content
        with open(first_output_path, "r") as file:
            first_content = file.read()
            self.assertIn("user_id", first_content)

        with open(second_output_path, "r") as file:
            second_content = file.read()
            self.assertIn("user_id", second_content)

    def test_main_day_filter(self):
        Config.OUTPUT_PATH = os.path.join(Config.OUTPUT_PATH, "day")
        main(input_path=self.input_file, filter_type=FilterType.DAY, filter_value=None)
        first_output_path = os.path.join(Config.OUTPUT_PATH, "first.csv")
        second_output_path = os.path.join(Config.OUTPUT_PATH, "second.csv")

        # Check if output files are created
        self.assertTrue(
            os.path.exists(first_output_path), "First output file not created!"
        )
        self.assertTrue(
            os.path.exists(second_output_path), "Second output file not created!"
        )

        # Optionally, you can read the files and assert on their content
        with open(first_output_path, "r") as file:
            first_content = file.read()
            self.assertIn("user_id", first_content)

        with open(second_output_path, "r") as file:
            second_content = file.read()
            self.assertIn("user_id", second_content)


if __name__ == "__main__":
    unittest.main()
