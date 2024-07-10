import csv
import logging
import os


logger = logging.getLogger(__name__)


class OutputManager:
    @staticmethod
    def write_to_csv(data, headers, output_location):
        if not os.path.exists(os.path.dirname(output_location)):
            os.makedirs(os.path.dirname(output_location))

        with open(output_location, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        logging.info(f"Data written to {output_location}")
