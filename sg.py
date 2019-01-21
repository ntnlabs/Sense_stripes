import sqlite3
import plotly
import plotly.graph_objs as go

# prepare database and others
conn = sqlite3.connect('/home/pi/Database/sensor_data.db')
c = conn.cursor()
timeline = []
hum_values = []
temp_values = []
pres_values = []

# get data (-1h = ~60 values) ##debug -> 7days = 60*24*7 = 10080
c.execute("SELECT * FROM HAT_table ORDER BY rowid DESC LIMIT 30240")
rows = c.fetchall()

for row in rows:
 timeline.insert(0,row[0]+', '+row[1])
 hum_values.insert(0,row[3])
 temp_values.insert(0,row[2])
 pres_values.insert(0,row[4])


trace1 = go.Scatter(
 x = timeline,
 y = hum_values,
 name = 'vlhkost',
 mode = 'lines'
)

trace2 = go.Scatter(
 x = timeline,
 y = temp_values,
 name = 'teplota',
 mode = 'lines' 
)

trace3 = go.Scatter(
 x = timeline,
 y = pres_values,
 name = 'tlak',
 mode = 'lines',
 yaxis = 'y2'
)

layout = go.Layout(
 title = "tlak, vlhkost, teplota (poslednych 21 dni)",
 xaxis = dict(type='category'),
 yaxis = dict(
  range = [20, 90],
  title = 'teplota,vlhkost'
 ),
 yaxis2 = dict(
  title = 'tlak',
  range = [900,1100], 
  overlaying = 'y',
  side = 'right'
 )
)

# put the data together
data = [trace1, trace2, trace3]
godata = dict(data=data, layout=layout)

plotly.offline.plot(godata, filename='/home/pi/weather/3weeks.html', auto_open=False)

#let's clean a bit...
conn.close()
