from datetime import datetime, timedelta
import unittest
from src.user.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("2e5d8815-4e59-4302-99c0-6fc9593a2eef")
        self.start_time = datetime.strptime(
            "2024-01-01T08:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        self.end_time = datetime.strptime(
            "2024-01-01T16:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ"
        )

    def test_incorrect_user_id(self):
        with self.assertRaises(ValueError) as context:
            User("1")

        self.assertTrue("Invalid user ID" in str(context.exception))

    def test_add_to_attendance(self):
        self.user.add_to_attendance("GATE_IN", "2024-01-01T08:00:00.000Z")
        self.assertEqual(len(self.user.attendance_data), 1)

    def test_incorrect_gate_in_sequence(self):
        with self.assertRaises(ValueError) as context:
            self.user.add_to_attendance("GATE_IN", "2024-01-01T08:00:00.000Z")
            self.user.add_to_attendance("GATE_IN", "2024-01-01T09:00:00.000Z")

        self.assertTrue(
            "GATE_IN must be preceded by GATE_OUT" in str(context.exception)
        )

    def test_incorrect_gate_out_sequence(self):
        with self.assertRaises(ValueError) as context:
            self.user.add_to_attendance("GATE_IN", "2024-01-01T08:00:00.000Z")
            self.user.add_to_attendance("GATE_OUT", "2024-01-01T09:00:00.000Z")
            self.user.add_to_attendance("GATE_OUT", "2024-01-01T10:00:00.000Z")

        self.assertTrue(
            "GATE_OUT must be preceded by GATE_IN" in str(context.exception)
        )

    def test_incorrect_gate_out_as_first_entry(self):
        with self.assertRaises(ValueError) as context:
            self.user.add_to_attendance("GATE_OUT", "2024-01-01T08:00:00.000Z")

        self.assertTrue(
            "The first attendance record must be 'GATE_IN'" in str(context.exception)
        )

    def test_get_attendance_statistics(self):
        self.user.add_to_attendance("GATE_IN", self.start_time)
        self.user.add_to_attendance("GATE_OUT", self.end_time)
        stats = self.user.get_attendance_statistics(self.start_time, self.end_time)
        self.assertEqual(stats["time"], 8)
        self.assertEqual(stats["days"], 1)

    def test_get_average_per_day(self):
        ts1 = datetime.now()
        ts2 = ts1 + timedelta(hours=4)
        ts3 = ts1 + timedelta(days=1)
        ts4 = ts3 + timedelta(hours=2)
        self.user.add_to_attendance("GATE_IN", ts1)
        self.user.add_to_attendance("GATE_OUT", ts2)
        self.user.add_to_attendance("GATE_IN", ts3)
        self.user.add_to_attendance("GATE_OUT", ts4)

        stats = self.user.get_attendance_statistics(ts1, ts4)

        self.assertEqual(float(stats["average_per_day"]), 3.000)

    def test_get_longest_work_session(self):
        self.user.add_to_attendance("GATE_IN", self.start_time)
        self.user.add_to_attendance("GATE_OUT", self.end_time)
        longest_session = self.user.get_longest_work_session(
            self.start_time, self.end_time
        )
        self.assertEqual(longest_session.total_seconds(), 8 * 3600)


if __name__ == "__main__":
    unittest.main()
