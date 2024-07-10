import argparse
from datetime import datetime, timedelta
import logging
import os

from config import Config
from datapao_io.input_parser import InputParser
from datapao_io.output_manager import OutputManager
from time_manager import TimeManager

# Could be read from a .env config
logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)


""" 
Following SOLID, it's a good idea to create an interface for the input parsing.
This way we can replace it with a different input type later if we want to 
allow something other, than a .csv input.
"""


def determine_filter_window(filter_type, filter_value):
    now = datetime.now()

    if filter_type == "year":
        start_time = datetime(filter_value, 1, 1)
        end_time = datetime(filter_value + 1, 1, 1) - timedelta(seconds=1)
    elif filter_type == "month":
        start_time = datetime(now.year, datetime.strptime(filter_value, "%B").month, 1)
        if start_time.month == 12:
            end_time = datetime(now.year + 1, 1, 1) - timedelta(seconds=1)
        else:
            end_time = datetime(now.year, start_time.month + 1, 1) - timedelta(
                seconds=1
            )
    elif filter_type == "week":
        # Start the delta from the Monday of the current week
        start_time = now - datetime.timedelta(days=now.weekday())
        start_time = datetime(start_time.year, start_time.month, start_time.day)
        end_time = start_time + datetime.timedelta(
            days=6, hours=23, minutes=59, seconds=59
        )
    elif filter_type == "day":
        start_time = datetime(now.year, now.month, now.day)
        end_time = start_time + datetime.timedelta(hours=23, minutes=59, seconds=59)

    return (start_time, end_time)


def main(input_path, filter_type, filter_value):

    start_time, end_time = determine_filter_window(filter_type, filter_value)

    if not input_path:
        input_path = os.path.join(Config.RESOURCES_PATH, "datapao_homework_2024.csv")

    parsed_input = InputParser.parse_input(input_path)

    time_manager = TimeManager(parsed_input)

    office_hours_statistics = time_manager.calculate_statistics(start_time, end_time)

    logger.info(office_hours_statistics)

    # longest_work_session = time_manager.get_longest_work_session(
    #     filter_type, filter_value
    # )

    # save the results of task 1 into a .csv
    OutputManager.write_to_csv(
        office_hours_statistics,
        ["user_id", "time", "days", "average_per_day", "rank"],
        os.path.join(Config.OUTPUT_PATH, "first.csv"),
    )

    # save the results of task 2 into a .csv
    # OutputManager.write_to_csv(
    #     longest_work_session,
    #     ["user_id", "session_length"],
    #     os.path.join(Config.OUTPUT_PATH, "second.csv"),
    # )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the main script")
    parser.add_argument(
        "-i",
        "--input_file",
        required=False,
        help="Path to the input file. Relative to the project root. If omitted, it will run on the example in the resources/ folder",
    )
    parser.add_argument(
        "-t",
        "--type",
        required=True,
        choices=["year", "month", "week", "day"],
        help="Filter type. allowed values: year, month, week, day.",
    )
    parser.add_argument(
        "-v",
        "--value",
        help="Filter on this value grouped by the type.",
    )

    args = parser.parse_args()
    input_file = args.input_file
    filter_type = args.type
    filter_value = args.value

    # validate the arguments
    if filter_type in ["year", "month"] and filter_value is None:
        parser.error(f"the --value argument is required when --type is {filter_type}")

    if filter_type == "year":
        try:
            filter_value = int(filter_value)
        except ValueError:
            parser.error(
                "the --value argument must be an integer when --type is 'year'"
            )

    try:
        # omit the value if you want to get the weekly or the daily reports
        if filter_type in ["week, day"]:
            main(input_file, filter_type, None)

        else:
            main(input_file, filter_type, filter_value)
    except Exception as e:
        logger.error("There was an error parsing the instructions.")
        logger.error(f"{e}")
