import plotly as py
import plotly.graph_objs as go

import mysql.connector
import pandas as pd

def billimg():
    conn = mysql.connector.connect(user='root', password='1', host='127.0.0.1', database='Bill')
    cursor = conn.cursor()
    cursor.execute('select * from daily_sum where  DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date ;')
    rows = cursor.fetchall()
    str(rows)[0:300]
    cursor.close()
    df = pd.DataFrame( [[ij for ij in i] for i in rows] )
    df.rename(columns={0: 'date',1: 'sum'}, inplace=True);
    df = df.sort_values(['date']);

    trace1 = go.Scatter(
        x=df['date'],
        y=df['sum'],
        mode = 'markers+lines',
    )

    layout = go.Layout(
        title='month bill',
        xaxis=dict( title='date' ),
        yaxis=dict( title='sum' )
        )

    data = [trace1]
    fig = go.Figure(data=data, layout=layout)
    py.offline.plot(fig, filename='templates/poem.html')

    return

