import argparse
from datetime import datetime, timedelta
from enum import Enum
import logging
import os
import string

from config import Config
from datapao_io.input_parser import InputParser
from datapao_io.output_manager import OutputManager
from time_manager.time_manager import TimeManager

# Could be read from a .env config
logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)


class FilterType(Enum):
    YEAR = "year"
    MONTH = "month"
    WEEK = "week"
    DAY = "day"
    CUSTOM = "custom"


def determine_filter_window(filter_type:string = None, filter_value:string = None, custom_window:string = None) -> tuple:
    start_time = None
    end_time=None


    if custom_window is not None:
        times = custom_window.split(":")
        if len(times) != 2:
            raise ValueError("Provided custom time format is invalid!")
        
        start_time = datetime.strptime(times[0], "%Y-%m-%d")
        end_time = datetime.strptime(times[1], "%Y-%m-%d")

    
    else:
        now = datetime.now()

        if filter_type == FilterType.YEAR:
            start_time = datetime(filter_value, 1, 1)
            end_time = datetime(filter_value + 1, 1, 1) - timedelta(seconds=1)
        # TODO: parse month even if it's not passed in its with its long name
        elif filter_type == FilterType.MONTH:
            start_time = datetime(now.year, datetime.strptime(filter_value, "%B").month, 1)
            if start_time.month == 12:
                end_time = datetime(now.year + 1, 1, 1) - timedelta(seconds=1)
            else:
                end_time = datetime(now.year, start_time.month + 1, 1) - timedelta(
                    seconds=1
                )
        elif filter_type == FilterType.WEEK:
            # Start the delta from the Monday of the current week
            start_time = now - timedelta(days=now.weekday())
            start_time = datetime(start_time.year, start_time.month, start_time.day)
            end_time = start_time + timedelta(
                days=6, hours=23, minutes=59, seconds=59
            )
        elif filter_type == FilterType.DAY:
            start_time = datetime(now.year, now.month, now.day)
            end_time = start_time + timedelta(hours=23, minutes=59, seconds=59)

    if start_time is None or end_time is None:
        raise ValueError("Incorrect filter window!")
    
    logger.info(f"Filtering attendance records between {start_time} and {end_time}")

    return (start_time, end_time)



def main(input_path:string = None, filter_type:string = None, filter_value:string = None, custom_window:string = None):

    start_time =  None
    end_time = None
    
    if custom_window:
        start_time, end_time = determine_filter_window(custom_window=custom_window)

    else:
        start_time, end_time = determine_filter_window(filter_type, filter_value)

    if not input_path:
        input_path = os.path.join(Config.RESOURCES_PATH, "datapao_homework_2024.csv")

    if not os.path.exists(input_path):
        if os.path.exists(os.path.join(Config.RESOURCES_PATH, input_path)):
            input_path = os.path.join(Config.RESOURCES_PATH, input_path)
        else:
            raise FileNotFoundError("Invalid input file path!")

    """ 
    Following SOLID, it's a good idea to create an interface for the input parsing.
    This way we can replace it with a different input type later if we want to 
    allow something other, than a .csv input.
    """
    logger.info("Parsing input file..")
    parsed_input = InputParser.parse_input(input_path)

    logger.info('Creating Time manager..')
    time_manager = TimeManager(parsed_input)

    logger.info('Calculating office hours statistics..')
    office_hours_statistics = time_manager.calculate_statistics(start_time, end_time)

    # save the results of task 1 into a .csv
    OutputManager.write_to_csv(
        office_hours_statistics,
        ["user_id", "time", "days", "average_per_day", "rank"],
        os.path.join(Config.OUTPUT_PATH, "first.csv"),
    )
    logger.info(f'Office hour statistics are now available at: {Config.OUTPUT_PATH + 'first.csv'} !')


    logger.info('Calculating the longest work session..')
    longest_work_session = time_manager.get_longest_work_session(start_time, end_time)


    # save the results of task 2 into a .csv
    OutputManager.write_to_csv(
        longest_work_session,
        ["user_id", "session_length"],
        os.path.join(Config.OUTPUT_PATH, "second.csv"),
    )

    logger.info(f'Longest work session is available at: {Config.OUTPUT_PATH + 'second.csv'} !')



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
        choices=["year", "month", "week", "day", "custom"],
        help="Filter type. allowed values: year, month, week, day. Week and day gets the report for the current week/day, month for the specified month, year for the specified year.",
    )
    parser.add_argument(
        "-v",
        "--value",
        help="Filter on this value grouped by the type. In case you're filtering for months, use the full name of the month.",
    )

    parser.add_argument(
        "-c", 
        "--custom_range", 
        help="This flag allows you to add a custom date range as a filter. The format is: YYYY-MM-DD:YYYY-MM-DD",
        )

    args = parser.parse_args()
    input_file = args.input_file
    filter_type = FilterType(args.type)
    filter_value = args.value
    custom=args.custom_range

    # validate the arguments
    if filter_type in [FilterType.YEAR, FilterType.MONTH] and filter_value is None:
        parser.error(f"the --value argument is required when --type is {filter_type}")

    if filter_type == FilterType.YEAR:
        try:
            filter_value = int(filter_value)
        except ValueError:
            parser.error(
                "the --value argument must be an integer when --type is 'year'"
            )

    try:
        if filter_type == FilterType.CUSTOM:
            main(custom_window = custom)
        # omit the value if you want to get the weekly or the daily reports
        elif filter_type in [FilterType.WEEK, FilterType.DAY]:
            main(input_file, filter_type, None)

        else:
            main(input_file, filter_type, filter_value)
    except Exception as e:
        logger.error("There was an error parsing the instructions.")
        logger.error(f"{e}")
