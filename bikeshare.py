import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    while city not in CITIES:
        print('What city would you like to see data for?')
        city = input('Enter Chicago, New York City, or Washington: ').lower()

    # get user input for month (all, january, february, ... , june)
    month = None
    while month not in MONTHS and month != 'all':
        print('What month would you like to see data for?')
        month = input('Enter any month from January to June, or \'all\' to see data for all months: ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    while day not in DAYS and day != 'all':
        print('What day of the week would you like to see data for?')
        day = input('Enter any day of the week, or \'all\' to see data for all days: ').lower()

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

    city_file = CITY_DATA[city]
    df = pd.read_csv(city_file)

    df['start_dt'] = pd.to_datetime(df['Start Time'])
    df['end_dt'] = pd.to_datetime(df['End Time'])
    df['month'] = df['start_dt'].dt.month
    df['day'] = df['start_dt'].dt.weekday
    df['travel_times'] = df['end_dt'].sub(df['start_dt'])

    if month != 'all':

        month_ind = MONTHS.index(month) + 1
        df = df[df['month'] == month_ind]

    if day != 'all':

        day_ind = DAYS.index(day)
        df = df[df['day'] == day_ind]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month_ind = df['month'].mode()[0] - 1
    popular_month = MONTHS[popular_month_ind]
    print('The most popular month for bike trips is:', popular_month)

    # display the most common day of week
    popular_day_ind = df['day'].mode()[0]
    popular_day = DAYS[popular_day_ind]
    print('The most popular day for bike trips is:', popular_day)

    # display the most common start hour
    df['hour'] = df['start_dt'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour to start bike trips is:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most start station is:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most end station is:', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Start/End'] = df['Start Station'].map(str) + ", " + df['End Station']
    popular_pair = df['Start/End'].mode()[0]

    print('The most common bike trips start/end at:', popular_pair)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['travel_times'].sum()
    print('The total travel time for all bike rides is:', str(total_travel_time))

    # display mean travel time
    avg_travel_time = df['travel_times'].mean()
    print('The average travel time for all bike rides is:', str(avg_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Here is a breakdown of the user types for bike rides')
    print(df['User Type'].value_counts())

    # Display counts of gender

    if 'Gender' in df:
        print('Here is a breakdown of the gender of bike rides')
        print(df['Gender'].value_counts())
    else:
        print('Gender data not available for this location')


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = df['Birth Year'].min()
        latest_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]

        print('The earliest birth year for a ride is:', earliest_birth)
        print('The most recent birth year for a rider is:', latest_birth)
        print('The most common birth year for all riders is:', most_common_birth)
    else:
        print('Birth year data not available for this location')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays 5 random rows of the dataframe so users can see raw data"""
    rows = df.sample(5).to_dict('records')
    for row in rows:
        print(row)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            print('Would you like to see 5 random rows of individual trip data?')
            raw_data = input('Enter yes or no: ')
            if raw_data.lower() == 'no':
                break
            elif raw_data.lower() == 'yes':
                display_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
