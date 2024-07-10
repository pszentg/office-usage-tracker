from datetime import datetime, timedelta
import string

from config import Config
from user.user import User


class TimeManager:
    def __init__(self, parsed_input: list):
        self.users = {}
        # create the users
        for row in parsed_input:
            # this isn't necessarily needed because the user object has an id
            # but saving like this makes fetching a specific user on the time manager
            # makes the runtime O(1) complex.
            user_id = row["user_id"]
            if user_id not in self.users:
                self.users[user_id] = User(user_id)

        # record their attendance data
        for row in parsed_input:
            user_id = row["user_id"]
            # get the TIMESTAMP_FORMAT from the config. The example defined ISO-8601.
            # This will throw an error for other formats.
            event_date = datetime.strptime(row["event_time"], Config.TIMESTAMP_FORMAT)
            self.users[user_id].add_to_attendance(
                str.upper(row["event_type"]), event_date
            )

    def calculate_statistics(self, start_time: string, end_time: string) -> dict:
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

    def format_longest_work_session(self, session: timedelta) -> string:
        s = session.seconds
        h, remainder = divmod(s, 3600)
        m, s = divmod(remainder, 60)

        return f"{h}H:{m}m:{s}s"

    def get_longest_work_session(self, start_time: str, end_time: str) -> dict:
        longest_session = timedelta(0)
        longest_user_id = None

        for user_id, user in self.users.items():
            user_longest_session = user.get_longest_work_session(start_time, end_time)
            if user_longest_session > longest_session:
                longest_session = user_longest_session
                longest_user_id = user_id

        formatted_longest_session = self.format_longest_work_session(longest_session)

        return {"user_id": longest_user_id, "session_length": formatted_longest_session}
