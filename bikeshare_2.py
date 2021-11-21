import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # initializing variables
    city = None
    month = None
    day = None
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city != "chicago" and city != "new york city" and city != "washington":
        city = input(
            "Enter a city (chicago, new york city , washington): ").lower()
    # get user input for month (all, january, february, ... , june)
    while month != "all" and month != "january" and month != "february"\
            and month != "march" and month != "april" and month != "may"\
            and month != "june":
        month = input(
            "If you want to filter by month Enter->(january, february, march, april, may, june) or no filter Enter->(all) ").lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while day != 'all' and day != 'sunday' and day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday':
        day = input(
            "If you want to filter by day Enter a day e.g.(Tuesday) or no filter Enter (all) ").lower()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # opening csv using pandas
    df = pd.read_csv(CITY_DATA[city])
    # operating on df to start filtering ...
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day != 'all':
        #day_index = int(day)-1
        # days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        #        'Friday', 'Saturday']
        #day_name = days[day_index]
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['January', 'February', 'March', 'April', 'April', 'June']
    month_num = df['month'].mode()[0]
    month_name = months[month_num-1]
    print("The most common month in this dataset-> ", month_name)
    # display the most common day of week
    print(
        "The most common day of week in this dataset-> ", df['day_of_week'].mode()[0])
    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    pop_hour = df['hour'].mode()[0]
    print("The most common hour in this dataset-> ", round(pop_hour, 2))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    # .max() here returns the value of the series, while I need the station name so after searching use .idxmax()
    common_start = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start stations-> ", common_start)
    # display most commonly used end station
    common_end = df['End Station'].value_counts().idxmax()
    print("The most commonly used end stations-> ", common_end)
    # display most frequent combination of start station and end station trip
    freq_comb = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("The most frequent combination stations are")
    print("Start station-> ", freq_comb.idxmax()[0])
    print("End station-> ", freq_comb.idxmax()[1])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # as the sum will be a large number I will convert it to hours and days both
    total_time = df['Trip Duration'].sum()
    print("Total travel time-> ", round(total_time/(60*60), 2), " Hours")
    print("Total travel time-> ", round(total_time/(60*60*60), 2), " Days")
    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Mean time-> ", round(mean_time/60, 2), " Hours")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print(user_type)
    # Display counts of gender
    try:
        gender_type = df['Gender'].value_counts()
        print(gender_type)
    except Exception:
        print("Sorry no Gender data available for this city :)")
    # Display earliest, most recent, and most common year of birth
    try:
        print("Most common year of birth is: ",
              int(df['Birth Year'].mode()[0]))
        print("Eariliest year of birth is: ", int(df['Birth Year'].min()))
        print("Most recent year of birth is: ", int(df['Birth Year'].max()))
    except Exception:
        print("Sorry no Birth Year data available for this city :)")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    view_data = input(
        "Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    view_display = "yes"
    while(view_display == "yes"):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display=input("Do you wish to continue? (yes) (no): ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    print(CITY_DATA)


if __name__ == "__main__":
    main()
