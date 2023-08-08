# Import the necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Ask the user for the stock ticker
ticker = input("Enter the stock ticker: ")

# Request the stock data from the Alpha Vantage API
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey=API_KEY"
data = requests.get(url).json()

# Extract the stock data from the response
stock_data = data["Time Series (5min)"]

# Convert the data to a DataFrame
df = pd.DataFrame(stock_data).transpose()
df.index = pd.to_datetime(df.index)

# Use the linear regression model to make predictions
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(df[["1. open", "2. high", "3. low", "4. close"]], df["5. volume"])
predictions = model.predict(df[["1. open", "2. high", "3. low", "4. close"]])

# Plot the predictions on a chart
plt.plot(predictions, label="Predicted")
plt.plot(df["5. volume"], label="Actual")
plt.legend()
plt.show()
