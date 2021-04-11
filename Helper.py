import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml

def Y_m_d_to_unix_str(ymd_str):
    return str(int(time.mktime(pd.to_datetime(ymd_str).date().timetuple())))

def fetch_GSPC_data(start_date, end_date):
    URL='http://finance.yahoo.com/quote/IVV/history?'+\
           'period1='+ Y_m_d_to_unix_str(start_date) + \
                '&period2=' + Y_m_d_to_unix_str(end_date) + \
                '&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
    gspc_page = requests.get(URL)
    soup = BeautifulSoup(gspc_page.content, 'html.parser')
    table_html = soup.findAll('table', {'data-test': 'historical-prices'})
    df = pd.read_html(str(table_html))[0]
    df.drop(df.tail(1).index, inplace=True)
    df.Date = pd.to_datetime(df.Date)
    return df

# fetch_GSPC_data('2016/05/13', '2016/06/13')