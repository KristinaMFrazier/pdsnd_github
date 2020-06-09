import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Which city do you want to explore? Enter one of the following: chicago, new york city, or washington: ")
            break
        except:
            print('That\'s not a valid city - try again!')
        finally:
            print("Thank you!")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("For which month do you want to analyze? ").title()
            break
        except:
            print('That\'s not a valid month - try again!')
        finally:
            print("We will explore data for {}.".format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("And for which day of the week do you want to explore? ").title()
            break
        except:
            print('That\'s not a valid day - try again!')
        finally:
            print("We will explore data for {}.".format(day))

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
    # Load input city data into a data frame
    df = pd.read_csv(CITY_DATA[city])

    # Define new columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # Convert string month input to match integer values of new month column
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May','June','July','August','September','October','November','December']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # Convert day input to title case
    if day != 'all':
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        # filter by day of week to create the new dataframe
        day = days.index(day) + 1
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month of travel is: ",df['month'].mode())

    # TO DO: display the most common day of week
    print("The most common day of travel is: ",df['day_of_week'].mode())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is: ",df['hour'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is: ",df['Start Station'].mode())

    # TO DO: display most commonly used end station
    print("The most commonly used end station is: ",df['End Station'].mode())

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combo'] = 'FROM ' + df['Start Station'] + ' TO ' + df['End Station']
    print("The most frequent combination of start station and end station trip is: ",df['Station Combo'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time is: ",df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Mean travel time is: ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types is: ",df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
            print("Counts of gender is: ",df['Gender'].value_counts())
    except:
            print("There is no gender data in this dataset.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("The earliest birth year is: ", df['Birth Year'].min())
        print("The most recent birth year is: ", df['Birth Year'].max())
        print("The most common birth year is ", df['Birth Year'].mode())
    except:
        print("There is no birth year data in this dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city.lower(), month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        see_data = input('\nWould you like to see five rows of the raw data based on your filters? Enter yes or no.\n')
        if see_data.lower() == 'yes':
            # display 5 rows of data
            rows = 5
            print(df.iloc[0:rows])
            while True:
                # ask user to see more data
                see_more = input('\nWould you like to see more?\n')
                if see_more.lower() == 'yes':
                    # display the next five rows of data
                    print(df.iloc[rows:(rows+5)])
                else:
                    break
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
