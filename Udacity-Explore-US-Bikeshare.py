
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_name = ["chicago","new york city","washington"]
months= ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

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
        city= input("Please enter the city name to filter it:\n")
        city = city.lower()
        if city not in city_name:
            print("Please Enter a valied city name")
            continue
        elif city in city_name :
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please Enter the month name or "all" for get all record for all months:\n')
        month = month.lower()
        if month not in months:
            print("Please enter a valied month")
            continue
        elif month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please Enter the day name or "all" for get all record for all days:\n')
        day = day.lower()
        if day not in days:
            print("Please enter a valied day")
            continue
        elif day in days:
            break

    print("--------------------------------------------------------------------------------------------------------")
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
    df = pd.read_csv(CITY_DATA[city]) 
    
    df["Start Time"]= pd.to_datetime(df["Start Time"])
    
    df['month'] = df['Start Time'].dt.month
    
    df['day'] = df['Start Time'].dt.day_name()
    
    # filter by month to create the new dataframe
    if month != "all":
        month = months.index(month)+1   
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f'Most Common Month is {common_month}')
    print("The most common month is ", df['month'].mode()[0], "\n")

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print(f'Most Common Day is {common_day}')
    print("The most common day of week  is ", df['day'].mode()[0], "\n")
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f'Most Common Hour is {common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]
    print(f'Most Common Start Station is : {popular_start_station}')

    # TO DO: display most commonly used end station
    popular_end_station = df["End Station"].mode()[0]
    print(f'Most Common End Station is : {popular_end_station}')
    
    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " \ " + df['End Station']
    print(f'Most Common Start & End Stations are : {df["combination"].mode()[0]}')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(f"the total travel time is = {df['Trip Duration'].count()}")

    # TO DO: display mean travel time
    print(f"the mean travel time is = {df['Trip Duration'].mean()}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(f'The counts of user types: \n {df["User Type"].value_counts()}')

    # TO DO: Display counts of gender
    print(f'The counts of Gender: \n {df["Gender"].value_counts()}')

    # TO DO: Display earliest, most recent, and most common year of birth
    print(f'The most common year of birth: {df["Birth Year"].mode()[0]}')
    print(f'The most recent year of birth: {df["Birth Year"].max()}')
    print(f'The earliest year of birth: {df["Birth Year"].min()}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()





