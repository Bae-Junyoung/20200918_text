from django.shortcuts import render

# Create your views here.
import pandas as pd
import pymysql

def main_view(request):

    df = pd.read_csv(r'C:\Users\Bae Junyoung\OneDrive\Desktop\python\200821__\0915\covid19.csv')
    labels=list(map(str,df.stateDt.values.tolist()[1:]))
    data=df.new.values.tolist()[1:]
    return render(request, 'line-chart.html', {
        'labels': labels, 'data': data,
    })

def sub_view(request):

    con = pymysql.connect(host='192.168.191.100', user='root', password='qwer0000', charset='utf8', database='stock')
    df = pd.read_sql('SELECT * FROM seoul_pop WHERE STDR_DE_ID >="20200809" AND STDR_DE_ID<="20200818"', con=con)
    df1 = df[['TOT_LVPOP_CO', 'name']]
    df2 = df1.groupby('name')[['TOT_LVPOP_CO']].mean().reset_index()

    return render(request, 'bar-chart.html', {
        'labels': list(df2.name.values), 'data': list(df2.TOT_LVPOP_CO.values),
    })