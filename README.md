# datapao-assignment

A repository for the assignment for the interview with DATAPAO

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

## Task Requirements

Only core python libraries are allowed, the data can not be stored in SQLite. Jupyter notebooks are also disallowed.

### Output requirements

- /output/first.csv | Header: (user_id, time, days, average_per_day, rank)
- /output/second.csv | Header: (user_id, session_length)

## Project dependencies

The project was written using Python v3.12. Dependencies not included in core Python are not allowed, therefore no `pip install -r requirements.txt` or installing any packages is needed.

## Run the project

Add the project to your PYTHONPATH. Assuming you're in the root of this repository: `export PYTHONPATH=$(pwd)/src:$PYTHONPATH`.

Start the project from the project root with `python main.py -i <your_input_file> -t filter_type -v filter_value`. If you use the included input, use the following: `python main.py -i resources/datapao_homeword_2023.csv -t month -v February`.

## (optional)

You can also get the usage statistics for a specific year (assuming you have more in your input file): `python main.py -i resources/datapao_homeword_2023.csv -t year -v 2023`. You can use the report for 2023-24 in the `resources/`.

Get the reports for the current calendar week: `python main.py -i <your_csv_file_for_the_current_year>, -t week`.
Get the reports for the current day: `python main.py -i <your_csv_file_for_the_current_year>, -t day`.
Values supported with the last 2 options are omitted.

Getting the statistics for a specific year or the current calendar week/day was not part of the task explicitly, but it made sense to implement those too.

## Optional setup

Take a look at the config.py class. It offers a class that you can edit to access some config variables in a static way. In case the usage of external packages were allowed, I'd rather use `.env` files, this was the next best thing using core Python.

## Run the tests

Same idea, as running the project, set the PYTHONPATH: `export PYTHONPATH=$(pwd)/src:$PYTHONPATH`.
Then from the project root: `python -m unittest discover tests`

## Further improvements

- introducing .env management
- introducing pre-commit hooks to run black and make the code PEP-compliant
