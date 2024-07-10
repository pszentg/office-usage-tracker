import re
import string


class User:
    def __init__(self, id):
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

        self.attendance_data.append((event, timestamp))

    def get_attendance_statistics(self, filter_type: string, filter_value: string):
        pass

    def get_longest_work_session(self, filter_type: string, filter_value: string):
        pass
