import argparse
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


def main(input_path, filter_type, filter_value):
    if not input_path:
        input_path = os.path.join(Config.RESOURCES_ROOT, "datapao_homework_2023.csv")

    parsed_input = InputParser.parse_input(input_path)

    time_manager = TimeManager(parsed_input)

    office_hours_statistics = time_manager.calculate_statistics(
        filter_type, filter_value
    )

    # longest_work_session = time_manager.get_longest_work_session(
    #     filter_type, filter_value
    # )

    # # save the results of task 1 into a .csv
    # OutputManager.write_to_csv(
    #     office_hours_statistics,
    #     ["user_id", "time", "days", "average_per_day", "rank"],
    #     Config.TASK_1_OUTPUT,
    # )

    # # save the results of task 2 into a .csv
    # OutputManager.write_to_csv(
    #     longest_work_session, ["user_id", "session_length"], Config.TASK_2_OUTPUT
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
