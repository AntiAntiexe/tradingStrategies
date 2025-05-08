import yfinance as yf
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

def get_date_x_days_before(date_string, num_days_before):
    date_object = dt.datetime.strptime(date_string, "%Y-%m-%d")
    new_date = date_object - dt.timedelta(days=num_days_before)
    new_date_string = new_date.strftime("%Y-%m-%d")
    return new_date_string

stock       = "AAPL"
start_date  = "2025-04-10"
end_date    = "2025-04-10"
num_periods50 = 50
num_periods200 = 200


aapl = yf.Ticker(stock)


start_date_x_days_before = get_date_x_days_before(start_date, num_periods50*2)

aapl_hist = aapl.history(start=start_date_x_days_before, end=end_date, interval="1d")

aapl_hist["SMA50"] = aapl_hist['Close'].rolling(window=num_periods50).mean()

start_date_x_days_before = get_date_x_days_before(start_date, num_periods200*2)
aapl_hist["SMA200"] = aapl_hist['Close'].rolling(window=num_periods200).mean()

aapl_hist['Signal'] = 0  # Initialize Signal column with 0
aapl_hist.loc[aapl_hist['SMA50'] > aapl_hist['SMA200'], 'Signal'] = 1  # Buy
aapl_hist.loc[aapl_hist['SMA50'] < aapl_hist['SMA200'], 'Signal'] = -1  # Sell

aapl_hist['Position'] = aapl_hist['Signal'].shift(1)

aapl_hist['Daily Return'] = aapl_hist['Close'].pct_change()

aapl_hist['Strategy Return'] = aapl_hist['Position'] * aapl_hist['Daily Return']

# Calculate cumulative returns
aapl_hist['Cumulative Market Return'] = (1 + aapl_hist['Daily Return']).cumprod()
aapl_hist['Cumulative Strategy Return'] = (1 + aapl_hist['Strategy Return']).cumprod()






plt.plot(aapl_hist['Close'])
plt.plot(aapl_hist['SMA50'])
plt.plot(aapl_hist['SMA200'])
plt.plot(aapl_hist['Cumulative Strategy Return'])
plt.plot(aapl_hist['Cumulative Market Return'])
plt.legend(['Close', 'SMA50', 'SMA200', 'Strategy Return', 'Market Return'])
plt.title('AAPL Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

#print(aapl_hist)
print('DONE!')