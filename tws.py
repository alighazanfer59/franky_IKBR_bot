from ib_insync import *
# util.startLoop()  # uncomment this line when in a notebook

ib = IB()
ib.connect('127.0.0.1', 4002, clientId=1)

contract = Stock('AAPL','SMART','USD')
bars = ib.reqHistoricalData(
    contract, endDateTime='', durationStr='7 D',
    barSizeSetting='4 hours', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas dataframe (pandas needs to be installed):
df = util.df(bars)
print(df)