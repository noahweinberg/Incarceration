import plotly.graph_objs as go 
import plotly.offline as pyo 
import pandas as pd 

df = pd.read_excel(r'/Users/personal/Desktop/incarceration/State/statedata.xlsx')

fig = go.Figure(data=go.Choropleth(
    locations=df['Code'], # Spatial coordinates
    z = df['Prisoners'], # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Prisoners",
    text = 'Prisoners'
))

fig.update_layout(
    title_text = '2016 US Prisoners By State',
    geo_scope='usa', # limite map scope to USA
)

pyo.plot(fig, filename='map.html')



