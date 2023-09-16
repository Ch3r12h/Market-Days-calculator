# market-days

import datetime

def find_market_days(start_date, num_days):
    current_date = start_date
    for _ in range(num_days):
        current_date += datetime.timedelta(days=4)
        print("Market days:", current_date.strftime("%A, %d %B %Y"))

# DEfine the starting date
start_date = datetime.datetime(2023, 7, 26) # Wednesday 26th July 2023 (random market day i attended)

# Define the number of market days you want tot find
num_market_days = 50

# Find and print the next market days
find_market_days(start_date, num_market_days)