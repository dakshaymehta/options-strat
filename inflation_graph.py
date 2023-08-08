import matplotlib.pyplot as plt

# Create a list of the months
months = ['October 2021', 'November', 'December', 'January 2022', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October']

# Create a list of the inflation rates
rates = [6.2, 6.8, 7.0, 7.5, 7.9, 8.5, 8.3, 8.6, 9.1, 8.5, 8.3, 8.2, 7.7]

# Use matplotlib to create a line graph
plt.plot(months, rates)
plt.xlabel('Month')
plt.ylabel('Inflation Rate (%)')
plt.show()
