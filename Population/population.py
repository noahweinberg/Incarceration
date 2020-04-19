import plotly.graph_objects as go 
import plotly.offline as pyo 
import pandas as pd 

df = pd.read_excel(r'/Users/personal/Desktop/incarceration/Population/population.xlsx')
print(df.head())

trace = go.Bar(
    x = df['Race'],
    y = df['Percentage'],
    name = 'Percent of Americans',
)  

data =  [trace]

layout = go.Layout(
    title = 'US Population Composition by Race',
    xaxis_title = 'Race',
    yaxis_title = 'Percentage Of Population',
)

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig, filename='population.html')
