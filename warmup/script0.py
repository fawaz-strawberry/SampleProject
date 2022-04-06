import requests

#command line arguments: sys.argv

url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=YXW39J53DO5XGFGQ"
r = requests.get(url)
data = r.json()

print(data.keys())

print("-----------------")
print(data["Time Series (5min)"])

time_series = data["Time Series (5min)"]

for entry in time_series.keys():
    print(str(entry) + " --- " + str(time_series[entry]))
    print("\n\n")