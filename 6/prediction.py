import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt
import warnings
warnings.filterwarnings("ignore", message="The behavior of DatetimeProperties.to_pydatetime is deprecated")

# Load the dataset
df = pd.read_csv('train.csv')

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Summarize sales by date
df = df.groupby('date').agg({'sales': 'sum'}).reset_index()

# Rename columns for Prophet
df = df.rename(columns={'date': 'ds', 'sales': 'y'})

# Split the data into train and test sets
train_size = int(len(df) * 0.8)
train, test = df[:train_size], df[train_size:]

# Define holidays (example: add relevant holidays)
holidays = pd.DataFrame({
    'holiday': 'example_holiday',
    'ds': pd.to_datetime(['2013-12-25', '2014-12-25', '2015-12-25']),  # Add relevant dates
    'lower_window': 0,
    'upper_window': 1,
})

# Initialize and fit the Prophet model with holidays
model = Prophet(holidays=holidays, yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False)
model.add_country_holidays(country_name='US')  # Add country-specific holidays if relevant
model.fit(train)

# Make predictions
future = model.make_future_dataframe(periods=len(test))
forecast = model.predict(future)

# Extract the predictions for the test set
predictions = forecast['yhat'].iloc[-len(test):].values

# Calculate RMSE
rmse = sqrt(mean_squared_error(test['y'], predictions))
print(f'RMSE: {rmse}')

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(train['ds'], train['y'], label='Training Data')
plt.plot(test['ds'], test['y'], label='Actual Sales')
plt.plot(test['ds'], predictions, label='Predicted Sales', color='red')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Forecasting')
plt.legend()
plt.show()

# Plot the forecast components
model.plot_components(forecast)
plt.show()
