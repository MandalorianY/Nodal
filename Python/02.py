import plotly.express as px
import pandas as pd

data = pd.read_csv('data\chart_data.csv')
fig = px.line(data, x='date', y='League of legends', title='League of Legends popularity over the last 30 day')
fig.update_yaxes(title_text='Popularity')
fig.write_html(r'static\trend.html')
