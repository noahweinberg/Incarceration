import plotly.graph_objects as go 
import plotly.offline as pyo 
import pandas as pd 

df = pd.read_excel(r'/Users/personal/Desktop/incarceration/Population/prisonpopbycountry.xlsx')
print(df.head())

trace = go.Bar(
    y = df['Country'],
    x = df['per100'],
    hovertext = df['population'],
    orientation = 'h'

)  

data =  [trace]

layout = go.Layout(
    title = 'Prisoners Per 100,000 People by Country',
    yaxis=dict(
                autorange="reversed"),
    xaxis_title = 'Prisoners Per 100,000 People',
    yaxis_title = 'Country',
)


fig = go.Figure(data=data,layout=layout)

fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'})


pyo.plot(fig, filename='population.html')
