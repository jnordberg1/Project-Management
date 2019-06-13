# -*- coding: utf-8 -*-
"""
@author: Jacob Nordberg 
"""
import plotly
import plotly.plotly as py
import plotly.figure_factory as ff

import pandas as pd

plotly.tools.set_credentials_file(username='jnordberg1', api_key='d0un96Av8w2I9pPH5hAx')

# Import Feeder Table
xl      = pd.ExcelFile(r"C:\USS\United States Solar Corporation\Site Selection - Documents\Tasks\NM\SS Schedule\NMwbsPrivateLand.xlsx")
# Create DataFrame
df = xl.parse(xl.sheet_names[0])
df = df.sort_values(by=['Task Number'], ascending = False)
df = df.reset_index()
#df['Complete'] = df['Complete']*100.0
df = df[['Task','Task Number','Start','Finish','Complete','Duration']]


#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gantt_example.csv')

fig = ff.create_gantt(df, colors=['#e8e1be','#ff4500'], index_col='Complete', show_colorbar=True, bar_width=0.2, showgrid_x=True, showgrid_y=True)
fig['layout'].update(title="New Mexico Private Lands", 
   paper_bgcolor='rgba(192,192,192,.5)', 
   plot_bgcolor='rgba(192,192,192,.3)', 
   autosize=True,
   width=900, 
   height=900, 
   margin=dict(l=340),
   font=dict(family='Helvetica, monospace', color='#050505'))
py.iplot(fig, filename='NM Gantt Public Lands', world_readable=True)