import datetime
import string

from config import Config
from user import User


class TimeManager:
    def __init__(self, parsed_input: list):
        self.users = {}
        # create the users
        for row in parsed_input:
            user_id = row["user_id"]
            if user_id not in self.users:
                self.users[user_id] = User(user_id)

        # record their attendance data
        for row in parsed_input:
            user_id = row["user_id"]
            # get the TIMESTAMP_FORMAT from the config. The example defined ISO-8601.
            # This will throw an error for other formats.
            event_date = datetime.datetime.strptime(
                row["event_time"], Config.TIMESTAMP_FORMAT
            )
            self.users[user_id].add_to_attendance(
                str.upper(row["event_type"]), event_date
            )

    def calculate_statistics(self, start_time: string, end_time: string):
        statistics = {}
        for user in self.users.values():
            statistics[user.id] = user.get_attendance_statistics(start_time, end_time)

        # make it a list and sort it, saving the rank is trivial now
        sorted_statistics = sorted(
            statistics.items(), key=lambda x: x[1]["average_per_day"], reverse=True
        )

        # arrange them in the expected format of the output
        sorted_statistics_dict = [
            {"user_id": user_id, "rank": index + 1, **stats}
            for index, (user_id, stats) in enumerate(sorted_statistics)
        ]

        return sorted_statistics_dict
