from pytrends.request import TrendReq


pytrend = TrendReq()
kw_list = ["League of legends"]
pytrend.build_payload(kw_list, cat=0, timeframe='today 1-m', geo='KR')
interest_over_time_df = pytrend.interest_over_time()
chart_data = interest_over_time_df.to_csv()
# save data
interest_over_time_df.to_csv('data\chart_data.csv')