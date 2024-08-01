# Office time tracker

This is a project that simulates an office tracking people entering and leaving the premises and offering some insights of your office usage.

## The task description

In the file in `resources/` you can find data of IoT devices related to 25 people. Using this data:

1. For each person calculate the amount of time and number of days spent in the office during February and write it to a CSV file containing `(user_id, time, days, average_per_day, rank)`

   - user_id - id of the user
   - time - net hours spent in the office (IN 8, OUT 12, IN 13, OUT 18) → this is 4 + 5 = 9 hours
   - days - the number of calendar days the user was present in the office
   - average_per_day - time/days
   - rank - order the employees based on the average_per_day (using Ordinal ranking)

2. Calculate who had the longest work session in February and write it to a CSV file containing (user_id, session_length)

   - user_id - id of the user
   - session_length - a work session is a time between coming to the office and leaving to go home (an office exit with no re-entry for two hours counts as going home, thus marking the end of a work session). Breaks shorter than two hours count as part of the session.
     - e.g. IN 8, OUT 12, IN 13, OUT 18, (IN next day) → this counts as one session from 8 to 18
     - eg. IN 8, OUT 12, IN 15, OUT 18, (IN next day) → these count as two sessions from 8 to 12 and from 15 to 18

3. (optional) You have the data. Please show us your ideas. It’s an opportunity to propose an insight you think would be valuable.
   - handle different input types, eg. `.txt`
   - implement a filter for different time ranges, eg. yearly, weekly, and daily.
   - implement a filter for custom date ranges.

### Output requirements

- `/output/office_statistics.csv` | Header: (user_id, time, days, average_per_day, rank)
- `/output/longest_work_session.csv` | Header: (user_id, session_length)

## Project dependencies

After activating your virtual environment, run `pip install -r requirements.txt`

## Run the project

Add the project to your PYTHONPATH. Assuming you're in the root of this repository: `export PYTHONPATH=$(pwd)/src:$PYTHONPATH`.

Start the project from the project root with `python main.py -i <your_input_file> -t filter_type -v filter_value`. If you use the included input, use the following: `python main.py -i resources/input_2023-24.csv -t month -v February`.

## (optional)

You can also get the usage statistics for a specific year (assuming you have more in your input file): `python main.py -i resources/input_2023-24.csv -t year -v 2023`. You can use the report for 2023-24 in the `resources/`.

Get the reports for the current calendar week: `python main.py -i <your_csv_file_for_the_current_year>, -t week`.
Get the reports for the current day: `python main.py -i <your_csv_file_for_the_current_year>, -t day`.
Get the reports for a custom time window: `python main.py -i <your_csv_file_for_the_current_year>, -t custom -v YYYY-MM-DD:YYYY-MM-DD`.

Note that the time format for the custom filter can be altered using the `.env` file.

Values supported with the last 2 options are omitted.

Getting the statistics for a custom time window, specific year or the current calendar week/day was not part of the task explicitly, but it made sense to implement those too.

## Run the tests

Same idea, as running the project, set the PYTHONPATH: `export PYTHONPATH=$(pwd)/src:$PYTHONPATH`.
Then from the project root: `python -m unittest discover tests`

## Further improvements

- introducing pre-commit hooks to run black and make the code PEP-compliant
