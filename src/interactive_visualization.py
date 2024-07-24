import pandas as pd
import plotly.express as px

# Load the dataset
file_path = 'dataset\stock_prices.csv'
stock_data = pd.read_csv(file_path)

# Convert the 'Date' column to datetime format
stock_data['Date'] = pd.to_datetime(stock_data['Date'])

# Create an interactive line plot for the stock prices
fig = px.line(stock_data, x='Date', y=['Open', 'High', 'Low', 'Close'],
              title='Stock Price Trends Over Time',
              labels={'value': 'Price', 'variable': 'Stock Metric'},
              template='plotly_dark')

fig.show()
