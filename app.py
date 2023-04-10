# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:57:59 2022

@author: agath
"""

import pandas as pd
import plotly_express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import os



df = pd.read_csv("https://raw.githubusercontent.com/cagatha/final_project/main/combine_all.csv",encoding='Big5')

del df[df.columns[0]]
print(df.head)

#print (df.dtypes)
df['price']= df['price'].str.replace(",","")
df['price'] = df['price'].astype(float)
df['rate_ppl']= df['rate_ppl'].str.replace(",","")
df['rate_ppl'] = df['rate_ppl'].astype(float)
df['checkoutd'] = df['checkoutd'].astype(str)
df['price_mean'] = df['price'].mean()
print(df.head)

app = dash.Dash()


#tab1
figbox = px.box(df, x="city", y="price",hover_name="city",title="Analysis of Prices with Different Cities",width=1600, height=800)
figbox2=figbox.add_shape( # add a horizontal "target" line
    type="line", line_color="red", line_width=3, opacity=0.7, line_dash="dash",
    x0=0, x1=1, xref="paper", y0=2720, y1=2720, yref="y")


#tab2
fighistogram=px.histogram(df,x="checkoutd",y="price",color="city",
                 title="Prices by Check-in Date: December 2022",
                 labels={"checkoutd":"Day of the Month"},
                  category_orders={ 
                "checkoutd": ["1", "2", "3", "4","5","6","7","8","9","10","11","12","13","14","15",
                              "16","17","18","19","20","21","22","23","24","25","26","27","28","29","30",
                              "31"]})


#tab3
figscatter = px.scatter(df, x="rate_ppl", y="rating", size='rate_ppl',
                        title="Relationship btw People and Ratings", 
                        labels={"rate_ppl":"Number of people who rate"},
    hover_data=['rate_ppl'],trendline="ols")

#tab4
figheat=px.density_heatmap(df, x="rating", y="price",template="seaborn",
                           title="Analysis of Prcies and Ratings")





app.layout = html.Div(
    [dcc.Tabs([
        dcc.Tab(dcc.Graph(figure=figbox2),label="Box Plot"),
        dcc.Tab(dcc.Graph(figure=fighistogram),label="Histogram"),
        dcc.Tab(dcc.Graph(figure=figscatter),label="Scatter Plot"),
        dcc.Tab(dcc.Graph(figure=figheat),label="Heatmap"),
             ]
)
]
)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0',port=port)