import pandas as pd
import plotly.express as px
from pytrends.request import TrendReq

pytrend = TrendReq()
kw_list = ["League of legends"]
pytrend.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='KR')
interest_over_time_df = pytrend.interest_over_time()
interest_over_time_df.rename(columns={'League of legends': 'Popularity'}, inplace=True)
interest_over_time_df.to_csv(r'data\chart_data.csv')

