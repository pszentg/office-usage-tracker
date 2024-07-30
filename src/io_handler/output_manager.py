import csv
import logging
import os


logger = logging.getLogger(__name__)


class OutputManager:
    @staticmethod
    def write_to_csv(data, headers, output_location) -> None:
        if not os.path.exists(os.path.dirname(output_location)):
            os.makedirs(os.path.dirname(output_location))

        try:
            with open(output_location, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()

                # Check if data is a list of dictionaries or a single dictionary
                if isinstance(data, list):
                    for row in data:
                        writer.writerow(row)
                elif isinstance(data, dict):
                    writer.writerow(data)
                else:
                    raise ValueError(
                        "Data is neither a list of dictionaries nor a single dictionary"
                    )

            logging.info(f"Data written to {output_location}")
        except Exception as e:
            logging.error(f"Failed to save data to CSV: {e}")
