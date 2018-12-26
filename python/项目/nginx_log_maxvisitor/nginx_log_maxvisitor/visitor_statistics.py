import plotly as py
import plotly.graph_objs as go

import mysql.connector
import pandas as pd

def visitor_statistics(dbuser,dbpassword,dbhost,dbbame,dbdate1,dbdate2,serverid,outfilename):
    conn = mysql.connector.connect(user=dbuser, password=dbpassword, host=dbhost, database=dbbame)
    cursor = conn.cursor()
    cursor.execute('select MAX(visitors) as maxvisitors,DATE_FORMAT(nginxdate,"%m%d") as nginxdate from visitor where nginxdate BETWEEN %s and %s and serverid = %s GROUP BY nginxdate;' ,(dbdate1,dbdate2,serverid))
    rows = cursor.fetchall()
    str(rows)[0:300]
    cursor.close()
    df = pd.DataFrame( [[ij for ij in i] for i in rows] )
    df.rename(columns={0: 'maxvisitors',1: 'nginxdate'}, inplace=True);
    df = df.sort_values(['nginxdate']);

    trace1 = go.Scatter(
        x=df['nginxdate'],
        y=df['maxvisitors'],
        mode = 'markers+lines',
    )

    layout = go.Layout(
        title='maxvisitor',
        xaxis=dict( title='nginxdate' ),
        yaxis=dict( title='maxvisitors' )
        )

    data = [trace1]
    fig = go.Figure(data=data, layout=layout)
    py.offline.plot(fig, filename=outfilename)

    return

