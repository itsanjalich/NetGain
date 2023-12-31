# -*- coding: utf-8 -*-
"""Netflix Stock Price Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MRKqj14iyntFgyMA7wfrZODWy0gVS3cr

Import Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error, r2_score

import os
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("/content/NFLX.csv")

df.head(10)

viz = df.copy()

df.isnull().sum()

df.shape

df.info()

df.describe().T

train, test = train_test_split(df, test_size = 0.2)

test_pred = test.copy()

train.head(10)

test.head(10)

x_train = train[['Open', 'High', 'Low', 'Volume']].values
x_test = test[['Open', 'High', 'Low', 'Volume']].values

y_train = train['Close'].values
y_test = test['Close'].values

model_lnr = LinearRegression()
model_lnr.fit(x_train, y_train)

y_pred = model_lnr.predict(x_test)

result = model_lnr.predict([[262.000000, 267.899994, 250.029999, 11896100]])
print(result)

print("MSE",round(mean_squared_error(y_test,y_pred), 3))
print("RMSE",round(np.sqrt(mean_squared_error(y_test,y_pred)), 3))
print("MAE",round(mean_absolute_error(y_test,y_pred), 3))
print("MAPE",round(mean_absolute_percentage_error(y_test,y_pred), 3))
print("R2 Score : ", round(r2_score(y_test,y_pred), 3))

def style():
    plt.figure(facecolor='black', figsize=(15,10))
    ax = plt.axes()

    ax.tick_params(axis='x', colors='white')    #setting up X-axis tick color to white
    ax.tick_params(axis='y', colors='white')    #setting up Y-axis tick color to white

    ax.spines['left'].set_color('white')        #setting up Y-axis spine color to white
    #ax.spines['right'].set_color('white')
    #ax.spines['top'].set_color('white')
    ax.spines['bottom'].set_color('white')      #setting up X-axis spine color to white

    ax.set_facecolor("black")                   # Setting the background color of the plot using set_facecolor() method

viz['Date']=pd.to_datetime(viz['Date'],format='%Y-%m-%d')

data = pd.DataFrame(viz[['Date','Close']])
data=data.reset_index()
data=data.drop('index',axis=1)
data.set_index('Date', inplace=True)
data = data.asfreq('D')
data

style()

plt.title('Closing Stock Price', color="white")
plt.plot(viz.Date, viz.Close, color="#94F008")
plt.legend(["Close"], loc ="lower right", facecolor='black', labelcolor='white')

style()

plt.scatter(y_pred, y_test, color='red', marker='o')
plt.scatter(y_test, y_test, color='blue')
plt.plot(y_test, y_test, color='lime')

test_pred['Close_Prediction'] = y_pred
test_pred

test_pred[['Close', 'Close_Prediction']].describe().T

test_pred['Date'] = pd.to_datetime(test_pred['Date'],format='%Y-%m-%d')

output = pd.DataFrame(test_pred[['Date', 'Close', 'Close_Prediction']])
output = output.reset_index()
output = output.drop('index',axis=1)
output.set_index('Date', inplace=True)
output =  output.asfreq('D')
output

output.to_csv('Close_Prediction.csv', index=True)
print("CSV successfully saved!")