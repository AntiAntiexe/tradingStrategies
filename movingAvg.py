import yfinance as yf
import matplotlib.pyplot as plt
import datetime as dt


def sma(ticker, start_date, end_date, num_periods):
    stock = ticker

    start_date_x_days_before = get_date_x_days_before(start_date, num_periods*2)

    stock_hist = stock.history(start=start_date_x_days_before, end=end_date, interval="1d")

    #stock_hist["SMA"+str(num_periods)] = stock_hist['Close'].rolling(window=num_periods).mean()

    sma_vals = stock_hist['Close'].rolling(window=num_periods).mean()

    return sma_vals
    

def get_date_x_days_before(date_string, num_days_before):
    date_object = dt.datetime.strptime(date_string, "%Y-%m-%d")
    new_date = date_object - dt.timedelta(days=num_days_before)
    new_date_string = new_date.strftime("%Y-%m-%d")
    return new_date_string

stock       = "AAPL"
start_date  = "2024-04-10"
end_date    = "2025-04-10"
#num_periods = 50


aapl = yf.Ticker(stock)

aapl_hist["SMA50"] = sma(aapl, start_date, end_date, 50)
aaple_hist = sma()



print(close_vals)
print(len(close_vals))


plt.plot(aapl_hist['Close'])
plt.plot(aapl_hist['SMA50'])
plt.legend(['Close', 'SMA50'])
plt.title('AAPL Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

#print(aapl_hist)
print('DONE!')