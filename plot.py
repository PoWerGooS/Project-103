import pandas as pd
import plotly.express as px
df=pd.read_csv('data.csv')
figure=px.scatter(df,x='country', y='cases', title="ScatterPlot")
figure.show()