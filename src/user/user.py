import re
import string
from datetime import timedelta


class User:
    def __init__(self, id) -> None:
        # The pattern in the example is similar to a GUID, but not specifically GUID.
        guid_pattern = r"[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}"

        if not re.match(guid_pattern, id):
            raise ValueError("Invalid user ID")

        self.id = id
        self.attendance_data = []

    def add_to_attendance(self, event: string, timestamp: string) -> None:
        if not self.attendance_data:
            if event != "GATE_IN":
                raise ValueError("The first attendance record must be 'GATE_IN'")
            self.attendance_data.append((event, timestamp))
            return

        last_event_type, _ = self.attendance_data[-1]
        if event == "GATE_IN" and last_event_type != "GATE_OUT":
            raise ValueError("GATE_IN must be preceded by GATE_OUT")
        elif event == "GATE_OUT" and last_event_type != "GATE_IN":
            raise ValueError("GATE_OUT must be preceded by GATE_IN")

        # TODO: it would be nice to store them in a sorted order, but that brings in further validation issues.
        self.attendance_data.append((event, timestamp))

    def get_attendance_statistics(self, start_time: str, end_time: str) -> dict:

        # a set can't have duplicate data - ideal to count the amount of individual days
        days_in_office = set()

        total_time = 0
        current_in_time = None

        for event, timestamp in self.attendance_data:
            if not (start_time <= timestamp <= end_time):
                continue

            if event == "GATE_IN":
                current_in_time = timestamp
                days_in_office.add(timestamp.date())
            elif event == "GATE_OUT" and current_in_time:
                total_time += (timestamp - current_in_time).total_seconds()
                current_in_time = None

        total_hours = total_time / 3600

        # truncate it at 3 decimals so it's more readable
        average_per_day = (
            "%.3f" % (total_hours / len(days_in_office)) if days_in_office else 0
        )

        return {
            "time": total_hours,
            "days": len(days_in_office),
            "average_per_day": average_per_day,
        }

    def get_longest_work_session(self, start_time: str, end_time: str) -> timedelta:

        longest_session = timedelta(0)
        current_in_time = None

        for event, timestamp in self.attendance_data:
            if not (start_time <= timestamp <= end_time):
                continue

            if event == "GATE_IN":
                current_in_time = timestamp
            elif event == "GATE_OUT" and current_in_time:
                session_duration = timestamp - current_in_time
                if session_duration > longest_session:
                    longest_session = session_duration
                current_in_time = None

        return longest_session
