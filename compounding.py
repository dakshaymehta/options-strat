# Import necessary modules
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Ask the user for the starting value and rate of compounding
startingValue = float(input("Enter the starting value: "))
rate = float(input("Enter the rate of compounding: "))

# Generate a sequence of dates
start = datetime.datetime.now()
end = datetime.datetime.strptime(input("Enter the ending date (YYYY-MM-DD): "), "%Y-%m-%d")
dates = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

# Calculate the compound interest
interest = startingValue * (1 + rate/100) ** len(dates)

# Create a data table to display the dates and compound interest values
data = {"Date": dates, "Price": interest}
table = pd.DataFrame(data)

print(table)

