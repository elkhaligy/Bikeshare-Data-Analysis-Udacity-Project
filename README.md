# Bikeshare Data Analysis Project

This project is part of the Udacity Data Analyst Nanodegree. It aims to perform data analysis on bikeshare data from three major cities in the United States: Chicago, New York City, and Washington. By using Python and Pandas, the project explores and analyzes bikeshare usage patterns and provides insights into the most frequent times of travel, the most popular stations, trip durations, and user statistics.

## Project Structure

- `bikeshare_2.py`: The main Python script containing functions to filter the data, load the data, and compute various statistics.

## Dependencies

The project requires the following Python libraries:
- `time`
- `pandas`

Make sure to install these libraries using pip if they are not already installed:

```sh
pip install pandas
```

## Datasets

The datasets used in this project are not included in the repository due to their size. You need to download the following CSV files and place them in the same directory as the script:

- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

## Usage

To run the project, simply execute the `bikeshare_2.py` script:

```sh
python bikeshare_2.py
```

The script will prompt you to enter a city, month, and day to filter the data. You can choose to filter by a specific city (Chicago, New York City, or Washington), by month (January to June), and by day of the week (Monday to Sunday). Alternatively, you can choose "all" to apply no filter for month and/or day.

After entering the filters, the script will display the following statistics:

1. **Time Statistics**: The most common month, day of the week, and start hour.
2. **Station Statistics**: The most commonly used start station, end station, and the most frequent combination of start and end stations.
3. **Trip Duration Statistics**: The total travel time and mean travel time.
4. **User Statistics**: Counts of user types, counts of gender (if available), and birth year statistics (if available).

You will also have the option to view individual trip data in increments of 5 rows.

## Function Descriptions

- `get_filters()`: Asks the user to specify a city, month, and day to analyze.
- `load_data(city, month, day)`: Loads data for the specified city and filters by month and day if applicable.
- `time_stats(df)`: Displays statistics on the most frequent times of travel.
- `station_stats(df)`: Displays statistics on the most popular stations and trip.
- `trip_duration_stats(df)`: Displays statistics on the total and average trip duration.
- `user_stats(df)`: Displays statistics on bikeshare users.
- `display_data(df)`: Displays 5 rows of individual trip data based on user input.
- `main()`: The main function that orchestrates the program flow.
