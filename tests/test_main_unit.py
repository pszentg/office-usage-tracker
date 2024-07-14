# import unittest
# from unittest.mock import patch, MagicMock
# from datetime import datetime
# import logging
# from main import main, determine_filter_window, FilterType


# class TestMainUnit(unittest.TestCase):

#     @patch("main.datetime")
#     @patch("main.InputParser")
#     @patch("main.TimeManager")
#     @patch("main.OutputManager")
#     @patch("main.Config")
#     @patch("main.logger")
#     def test_main_year_filter(
#         self,
#         mock_config,
#         mock_output_manager,
#         mock_time_manager,
#         mock_input_parser,
#         mock_datetime,
#     ):
#         # Setup mocks
#         mock_datetime.now.return_value = datetime(2024, 7, 13)
#         mock_config.RESOURCES_PATH = "resources"
#         mock_config.OUTPUT_PATH = "output"
#         mock_config.LOG_LEVEL = logging.DEBUG

#         mock_input_parser.parse_input.return_value = MagicMock()
#         mock_time_manager.return_value.calculate_statistics.return_value = [
#             {"user_id": 1, "time": 8, "days": 5, "average_per_day": 1.6, "rank": 1}
#         ]
#         mock_time_manager.return_value.get_longest_work_session.return_value = [
#             {"user_id": 1, "session_length": 5}
#         ]

#         with patch("main.os.path.exists") as mock_exists:
#             mock_exists.side_effect = [False, True]
#             main(filter_type=FilterType.YEAR, filter_value=2024)

#         # Assertions
#         mock_input_parser.parse_input.assert_called_once()
#         mock_time_manager.return_value.calculate_statistics.assert_called_once()
#         mock_time_manager.return_value.get_longest_work_session.assert_called_once()
#         mock_output_manager.write_to_csv.assert_any_call(
#             [{"user_id": 1, "time": 8, "days": 5, "average_per_day": 1.6, "rank": 1}],
#             ["user_id", "time", "days", "average_per_day", "rank"],
#             "output/first.csv",
#         )
#         mock_output_manager.write_to_csv.assert_any_call(
#             [{"user_id": 1, "session_length": 5}],
#             ["user_id", "session_length"],
#             "output/second.csv",
#         )

#     @patch("main.datetime")
#     @patch("main.InputParser")
#     @patch("main.TimeManager")
#     @patch("main.OutputManager")
#     @patch("main.Config")
#     @patch("main.logger")
#     def test_main_custom_filter(
#         self,
#         mock_config,
#         mock_output_manager,
#         mock_time_manager,
#         mock_input_parser,
#         mock_datetime,
#     ):
#         # Setup mocks
#         mock_datetime.now.return_value = datetime(2024, 7, 13)
#         mock_config.RESOURCES_PATH = "resources"
#         mock_config.OUTPUT_PATH = "output"
#         mock_config.LOG_LEVEL = logging.DEBUG

#         mock_input_parser.parse_input.return_value = MagicMock()
#         mock_time_manager.return_value.calculate_statistics.return_value = [
#             {"user_id": 1, "time": 8, "days": 5, "average_per_day": 1.6, "rank": 1}
#         ]
#         mock_time_manager.return_value.get_longest_work_session.return_value = [
#             {"user_id": 1, "session_length": 5}
#         ]

#         with patch("main.os.path.exists") as mock_exists:
#             mock_exists.side_effect = [False, True]
#             main(filter_type=FilterType.CUSTOM, filter_value="2024-01-01:2024-06-30")

#         # Assertions
#         mock_input_parser.parse_input.assert_called_once()
#         mock_time_manager.return_value.calculate_statistics.assert_called_once()
#         mock_time_manager.return_value.get_longest_work_session.assert_called_once()
#         mock_output_manager.write_to_csv.assert_any_call(
#             [{"user_id": 1, "time": 8, "days": 5, "average_per_day": 1.6, "rank": 1}],
#             ["user_id", "time", "days", "average_per_day", "rank"],
#             "output/first.csv",
#         )
#         mock_output_manager.write_to_csv.assert_any_call(
#             [{"user_id": 1, "session_length": 5}],
#             ["user_id", "session_length"],
#             "output/second.csv",
#         )

#     @patch("main.datetime")
#     @patch("main.InputParser")
#     @patch("main.TimeManager")
#     @patch("main.OutputManager")
#     @patch("main.Config")
#     @patch("main.logger")
#     def test_main_month_filter(
#         self,
#         mock_config,
#         mock_output_manager,
#         mock_time_manager,
#         mock_input_parser,
#         mock_datetime,
#     ):
#         # Setup mocks
#         mock_datetime.now.return_value = datetime(2024, 7, 13)
#         mock_config.RESOURCES_PATH = "resources"
#         mock_config.OUTPUT_PATH = "output"
#         mock_config.LOG_LEVEL = logging.DEBUG

#         mock_input_parser.parse_input.return_value = MagicMock()
#         mock_time_manager.return_value.calculate_statistics.return_value = [
#             {"user_id": 1, "time": 8, "days": 5, "average_per_day": 1.6, "rank": 1}
#         ]
#         mock_time_manager.return_value.get_longest_work_session.return_value = [
#             {"user_id": 1, "session_length": 5}
#         ]

#         with patch("main.os.path.exists") as mock_exists:
#             mock_exists.side_effect = [False, True]
#             main(filter_type=FilterType.MONTH, filter_value="July")

#         # Assertions
#         mock_input_parser.parse_input.assert_called_once()
#         mock_time_manager.return_value.calculate_statistics.assert_called_once()
#         mock_time_manager.return_value.get_longest_work_session.assert_called_once()
#         mock_output_manager.write_to_csv.assert_any_call(
#             [{"user_id": 1, "time": 8, "days": 5, "average_per_day": 1.6, "rank": 1}],
#             ["user_id", "time", "days", "average_per_day", "rank"],
#             "output/first.csv",
#         )
#         mock_output_manager.write_to_csv.assert_any_call(
#             [{"user_id": 1, "session_length": 5}],
#             ["user_id", "session_length"],
#             "output/second.csv",
#         )

#     @patch("main.datetime")
#     @patch("main.InputParser")
#     @patch("main.TimeManager")
#     @patch("main.OutputManager")
#     @patch("main.Config")
#     @patch("main.logger")
#     def test_main_week_filter(
#         self,
#         mock_config,
#         mock_output_manager,
#         mock_time_manager,
#         mock_input_parser,
#         mock_datetime,
#     ):
#         # Setup mocks
#         mock_datetime.now.return_value = datetime(2024, 7, 13)
#         mock_config.RESOURCES_PATH = "resources"
#         mock_config.OUTPUT_PATH = "output"
#         mock_config.LOG_LEVEL = logging.DEBUG

#         mock_input_parser.parse_input.return_value = MagicMock()
#         mock_time_manager.return_value.calculate_statistics.return_value = [
#             {"user_id": 1, "time": 8, "days": 5, "average_per_day": 1.6, "rank": 1}
#         ]
#         mock_time_manager.return_value.get_longest_work_session.return_value = [
#             {"user_id": 1, "session_length": 5}
#         ]

#         with patch("main.os.path.exists") as mock_exists:
#             mock_exists.side_effect = [False, True]
#             main(filter_type=FilterType.WEEK, filter_value=None)

#         # Assertions
#         mock_input_parser.parse_input.assert_called_once()
#         mock_time_manager.return_value.calculate_statistics.assert_called_once()
#         mock_time_manager.return_value.get_longest_work_session.assert_called_once()
#         mock_output_manager.write_to_csv.assert_any_call(
#             [{"user_id": 1, "time": 8, "days": 5, "average_per_day": 1.6, "rank": 1}],
#             ["user_id", "time", "days", "average_per_day", "rank"],
#             "output/first.csv",
#         )
#         mock_output_manager.write_to_csv.assert_any_call(
#             [{"user_id": 1, "session_length": 5}],
#             ["user_id", "session_length"],
#             "output/second.csv",
#         )

#     @patch("main.datetime")
#     @patch("main.InputParser")
#     @patch("main.TimeManager")
#     @patch("main.OutputManager")
#     @patch("main.Config")
#     @patch("main.logger")
#     def test_main_day_filter(
#         self,
#         mock_config,
#         mock_output_manager,
#         mock_time_manager,
#         mock_input_parser,
#         mock_datetime,
#     ):
#         # Setup mocks
#         mock_datetime.now.return_value = datetime(2024, 7, 13)
#         mock_config.RESOURCES_PATH = "resources"
#         mock_config.OUTPUT_PATH = "output"
#         mock_config.LOG_LEVEL = logging.DEBUG

#         mock_input_parser.parse_input.return_value = MagicMock()
#         mock_time_manager.return_value.calculate_statistics.return_value = [
#             {"user_id": 1, "time": 8, "days": 5, "average_per_day": 1.6, "rank": 1}
#         ]
#         mock_time_manager.return_value.get_longest_work_session.return_value = [
#             {"user_id": 1, "session_length": 5}
#         ]

#         with patch("main.os.path.exists") as mock_exists:
#             mock_exists.side_effect = [False, True]
#             main(filter_type=FilterType.DAY, filter_value=None)

#         # Assertions
#         mock_input_parser.parse_input.assert_called_once()
#         mock_time_manager.return_value.calculate_statistics.assert_called_once()
#         mock_time_manager.return_value.get_longest_work_session.assert_called_once()
#         mock_output_manager.write_to_csv.assert_any_call(
#             [{"user_id": 1, "time": 8, "days": 5, "average_per_day": 1.6, "rank": 1}],
#             ["user_id", "time", "days", "average_per_day", "rank"],
#             "output/first.csv",
#         )
#         mock_output_manager.write_to_csv.assert_any_call(
#             [{"user_id": 1, "session_length": 5}],
#             ["user_id", "session_length"],
#             "output/second.csv",
#         )


# if __name__ == "__main__":
#     unittest.main()
