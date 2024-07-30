import unittest
import os
import csv
from src.io_handler.output_manager import OutputManager


class TestOutputManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "./output/test_output.csv"
        self.data = [
            {
                "user_id": "1",
                "rank": 1,
                "total_hours": 8,
                "days_in_office": 1,
                "average_per_day": 8,
            }
        ]
        self.headers = [
            "user_id",
            "rank",
            "total_hours",
            "days_in_office",
            "average_per_day",
        ]

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_write_to_csv(self):
        OutputManager.write_to_csv(self.data, self.headers, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

        with open(self.test_file, mode="r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["user_id"], "1")


if __name__ == "__main__":
    unittest.main()
