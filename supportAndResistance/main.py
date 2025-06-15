import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


goog = yf.Ticker('goog')
data = goog.history(interval='1d', start='2024-01-01', end='2025-01-01')
print(data.head())

lowest = data['Close'].nsmallest(1).iloc[0]
second_lowest = data['Close'].nsmallest(2).iloc[1]

date_of_lowest = data['Close'].nsmallest(1).index[0]
date_of_sec_lowest = data['Close'].nsmallest(2).index[1]

xdiff = date_of_sec_lowest - date_of_lowest
ydiff = second_lowest - lowest

print(f"Lowest Close: {lowest} on {date_of_lowest}")
print(f"Second Lowest Close: {second_lowest} on {date_of_sec_lowest}")
lows = []

for i in range(len(data['Close'])):
    lows.append(data['Close'].nsmallest(i))

#print(lows)

plt.plot(date_of_lowest, lowest, 'ro', label='Lowest Close')
plt.plot(date_of_sec_lowest, second_lowest, 'bo', label='Second Lowest Close')
plt.plot(data['Close'])
#plt.gca().xaxis.set_major_locator(mdates.YearLocator(interval=1))
plt.title('GOOG Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

