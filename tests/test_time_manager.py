from datetime import datetime
import os
import sys
import unittest
from src.time_manager.time_manager import TimeManager

SRC_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src")
sys.path.insert(0, SRC_PATH)


class TestTimeManager(unittest.TestCase):
    def setUp(self):
        self.parsed_input = [
            {
                "user_id": "2e5d8815-4e59-4302-99c0-6fc9593a2eef",
                "event_type": "GATE_IN",
                "event_time": "2024-01-01T08:00:00.000Z",
            },
            {
                "user_id": "2e5d8815-4e59-4302-99c0-6fc9593a2eef",
                "event_type": "GATE_OUT",
                "event_time": "2024-01-01T16:00:00.000Z",
            },
            {
                "user_id": "2e5d8815-4e59-4302-99c0-6fc9593a2eef",
                "event_type": "GATE_IN",
                "event_time": "2024-01-02T10:00:00.000Z",
            },
            {
                "user_id": "2e5d8815-4e59-4302-99c0-6fc9593a2eef",
                "event_type": "GATE_OUT",
                "event_time": "2024-01-02T12:00:00.000Z",
            },
        ]
        self.time_manager = TimeManager(self.parsed_input)

        self.start_time = datetime.strptime(
            "2024-01-01T00:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        self.end_time = datetime.strptime(
            "2024-12-31T23:59:59.000Z", "%Y-%m-%dT%H:%M:%S.%fZ"
        )

    def test_calculate_statistics(self):

        stats = self.time_manager.calculate_statistics(self.start_time, self.end_time)
        self.assertEqual(len(stats), 1)
        self.assertEqual(stats[0]["time"], 10)
        self.assertEqual(stats[0]["days"], 2)
        self.assertEqual(float(stats[0]["average_per_day"]), 5.000)

    def test_get_longest_work_session(self):
        longest_session = self.time_manager.get_longest_work_session(
            self.start_time, self.end_time
        )
        self.assertEqual(longest_session["session_length"], "8H:0m:0s")


if __name__ == "__main__":
    unittest.main()
