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
            city = input("Please pick a city from: \n - Chicago \n - New York City \n - Washington \n to explore its data: \n").lower().strip()
            if city in ["chicago", "new york city", "washington"]:
                break
            else:
                print ("Sorry! it seems like you have entered an unavalible city, Can you please try again?")
        except:
                 print('Oops! Something went wrong,try something else.')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Would you like to filter the data by a specific month? or you'd like to view it all? \n").lower().strip()
            if month in ["january", "february", "march", "april", "may", "june", "all"]:
                break
            else:

                print ("Sorry! it seems like you have entered an unavalible month, Can you please try again?")
        except:
                 print('Oops! Something went wrong,try something else.')



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Would you like to filter the data by a specific day? or you'd like to view it all? \n").lower().strip()

            if day  in ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']:
                 break

            else:
                  print ("Sorry! it seems like you have entered an unavalible day, Can you please try again?")
        except:
               print('Oops! Something went wrong,try something else.')

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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])

    # extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    df["Start hour"] = df["Start Time"].dt.hour

    # filter by month if applicable
    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df["month"] == month]


    # filter by day of week if applicable
    if day != "all" :
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_frequent_month = df["month"].mode()[0]
    print (f"The most frequent month according to  your fillters of choice is:  {most_frequent_month} ")


    # TO DO: display the most common day of week
    most_frequent_day = df["day_of_week"].mode()[0]
    print (f"The most frequent day according to  your fillters of choice is: {most_frequent_day} ")


    # TO DO: display the most common start hour
    most_frequent_start_hour = df["Start hour"].mode()[0]
    print (f"The most frequent start hour according to  your fillters of choice is: {most_frequent_start_hour} ")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df["Start Station"].mode()[0]
    print(f"The most common start station is: {most_common_start_station} ")


    # TO DO: display most commonly used end station
    most_common_end_station = df["End Station"].mode()[0]
    print(f"The most common end station is: {most_common_end_station} ")

    # TO DO: display most frequent combination of start station and end station trip
    df["Stations Combined"]= df["Start Station"] + " " + df["End Station"]
    most_common_combination = df["Stations Combined"].mode()[0]
    print(f"The most common start & end station are: {most_common_combination}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print(f"The total travel time is: {total_travel_time} ")


    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print(f"The mean travel time is: {mean_travel_time} ")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df ["User Type"].value_counts()
    print(f"The total counts of user types is : {user_types_count} ")

    if city != 'washington':
        # TO DO: Display counts of gender
        gender_counts = df ["Gender"]. value_counts()
        print(f"The total counts of gender is: {gender_counts} ")


        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print(f"Earliest year: {earliest_year}\nMost recent year: {recent_year}\nMost frequent year: {common_year}")

    else:
         print('sorry, there\'s no gender or birth year data to be displayed')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)


        show_row = input('\nWould you like to see five lines of raw data? please enter yes or no.\n').lower().strip()
        x = 0
        if show_row == 'yes':
            print(df[x:x + 10])

            while True:
                x = x + 5
                show_row1 = input('\nWould you like to see five more? please enter yes or no.\n').lower().strip()
                if show_row1 == 'yes':
                    print(df[x:x + 5])
                else:
                     break

        restart = input('\nWould you like to restart? please enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
