import pandas as pd
import plotly.express as px

#Miss Nancy, The download worked! You just use plotly instead of plotly.express
# "pip3 install plotly". I was able to view the data and IT IS BEAUTIFUL. Oh,
# and the google sheets link did'nt work, so I had to use the data from WHO.

df = pd.read_csv("data.csv")
fig = px.scatter(df, x='Date_reported', y='Cumulative_cases', size="Cumulative_cases", color="Country", size_max=20)
fig.show()
