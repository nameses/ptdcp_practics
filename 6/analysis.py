import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Завантаження даних
df = pd.read_csv('train.csv')

# Перетворення дати в datetime
df['date'] = pd.to_datetime(df['date'])

# Сумування продажів за датою
df = df.groupby('date').agg({'sales': 'sum'}).reset_index()

# Відображення тренду
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['sales'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Trend Analysis')
plt.show()

# Проведення тесту Дікі-Фуллера
def adf_test(timeseries):
    print('Results of Augmented Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    print(dfoutput)

adf_test(df['sales'])

# Визначення оптимального порядку диференціювання
first_diff = df['sales'].diff().dropna()

# Повторне проведення тесту Дікі-Фуллера
adf_test(first_diff)

# Відображення автокореляції та часткової автокореляції
plt.figure(figsize=(12, 6))
plt.subplot(211)
plot_acf(first_diff, ax=plt.gca(), lags=40)
plt.subplot(212)
plot_pacf(first_diff, ax=plt.gca(), lags=40)
plt.show()
