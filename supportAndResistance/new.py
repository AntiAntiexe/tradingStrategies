import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


goog = yf.Ticker('goog')
data = goog.history(interval='1d', start='2024-01-01', end='2025-01-01')
print(data.head())


findTrend = np.polyfit(data.index.astype(int), data['Close'], 1)