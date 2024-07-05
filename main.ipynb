import pandas as pd
import numpy as np

#preprocessing this Data

df = pd.read_csv('stock_data.csv')
df.head(3)

df.isnull().sum()
df.describe()
# Data Visulization

import matplotlib.pyplot as plt
import seaborn as sns

# Set the date as the index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Plot the closing prices
plt.figure(figsize=(10, 5))
plt.plot(df['Close'], label='Close Price')
plt.title('Stock Close Price History')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.legend()
plt.show()

# Volume Analysis 
# Plot the volume traded
plt.figure(figsize=(10, 5))
plt.plot(df['Volume'], label='Volume')
plt.title('Stock Volume History')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.show()

# Calculate moving averages
df['SMA30'] = df['Close'].rolling(window=30).mean()
df['SMA100'] = df['Close'].rolling(window=100).mean()

# Plot the closing prices and moving averages
plt.figure(figsize=(10, 5))
plt.plot(df['Close'], label='Close Price')
plt.plot(df['SMA30'], label='30-Day SMA')
plt.plot(df['SMA100'], label='100-Day SMA')
plt.title('Stock Close Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.legend()
plt.show()
