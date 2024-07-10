import csv
import os


class InvalidCSVError(Exception):
    pass


class InputParser:
    """
    Input parser class.
    Parses the input file that contains the data.
    """

    REQUIRED_HEADERS = {"user_id", "event_type", "event_time"}

    @staticmethod
    def parse_input(input_path):
        if not os.path.exists(input_path):
            raise OSError("File does not exist!")

        if ".csv" in input_path:
            return InputParser.parse_csv_input(input_path)

        # we could implement other types of input here

    @staticmethod
    def parse_csv_input(input_path):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"{input_path} does not exist")

        with open(input_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            headers = set(reader.fieldnames)

            if not InputParser.REQUIRED_HEADERS.issubset(headers):
                raise InvalidCSVError(
                    f"CSV file must contain headers: {InputParser.REQUIRED_HEADERS}"
                )

            data = [row for row in reader]

        return data
