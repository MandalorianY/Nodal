import pandas as pd
import plotly.express as px


interest_over_time_df = pd.read_csv(r'data\chart_data.csv')
fig = px.line(interest_over_time_df, x='date', y='Popularity', title='League of Legends popularity over the last 90 day')
fig.write_html(r'static\trend_chart.html')