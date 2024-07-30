import csv
import os
import string


class InvalidCSVError(Exception):
    pass


class InputParser:
    """
    Input parser class.
    Parses the input file that contains the data.
    """

    REQUIRED_HEADERS = {"user_id", "event_type", "event_time"}

    @staticmethod
    def parse_input(input_path: string) -> list:
        if not os.path.exists(input_path):
            raise OSError("File does not exist!")

        if ".csv" in input_path:
            return InputParser.parse_csv_input(input_path)

        if ".txt" in input_path:
            return InputParser.parse_txt_input(input_path)

    @staticmethod
    def parse_csv_input(input_path: string) -> list:

        with open(input_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            headers = set(reader.fieldnames)

            if not InputParser.REQUIRED_HEADERS.issubset(headers):
                raise InvalidCSVError(
                    f"CSV file must contain headers: {InputParser.REQUIRED_HEADERS}"
                )

            data = [row for row in reader]

            for row in data:
                row["event_type"] = row["event_type"].upper()

        return data

    @staticmethod
    def parse_txt_input(input_path: string) -> list:
        with open(input_path, mode="r", newline="") as file:
            data = [line.strip().split(",") for line in file]

        # Ensure we have the correct number of columns and headers match
        headers = ["user_id", "event_type", "event_time"]
        parsed_data = []
        for row in data:
            if len(row) == len(headers):
                row_dict = {headers[i]: row[i] for i in range(len(headers))}
                row_dict["event_type"] = row_dict["event_type"].upper()
                parsed_data.append(row_dict)
            else:
                raise ValueError(f"Each row must have {len(headers)} columns")

        return parsed_data
