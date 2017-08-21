import numpy as np
import sys
import time;
import os
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

import matplotlib.pyplot as mpl
import matplotlib.collections as collections

def start_time(ha):
    start_time = datetime.today()
    start_time = start_time - timedelta(hours=ha)
    st_timestamp = int(float(time.mktime(start_time.timetuple()))) * 1000
    # print("Start time: {}".format(st_timestamp))
    return str(st_timestamp)

def end_time():
    end_time = datetime.today()
    et_timestamp = int(float(time.mktime(end_time.timetuple()))) * 1000;
    # print("End time: {}".format(et_timestamp))
    return str(et_timestamp)

def process_data(rows):
    rl=[]
    for r in rows:
        ta =0;
        if(r['orderType'] == 'BID'):
            ta = r['tradableAmount']
        else:
            ta = -r['tradableAmount']
        rl.append([r['tradeUid'], r['timestamp']/1000, ta * r['price']])

    c = ['id', 'timestamp', 'totalPrice']
    df = pd.DataFrame(rl, columns=c)
    return df

def plot_trade_data(df):
    #Timestamp data
    ts = df.timestamp.values
    #Number of x tick marks
    nTicks= 10
    #Left most x value
    s = np.min(ts)

    #Right most x value
    e = np.max(ts)

    #Total range of x values
    r = e - s
    #Add some buffer on both sides
    s -= r / 5
    e += r / 5
    #These will be the tick locations on the x axis
    tickMarks = np.arange(s, e, (e - s) / nTicks)

    #Convert timestamps to strings
    strTs = [datetime.fromtimestamp(i).strftime('%m-%d-%yT%H:%M:%S') for i in tickMarks]
    mpl.figure()
    #Plots of the tradable amount
    mpl.plot(ts, df.totalPrice.values, color = '#6495ed', linewidth = 1.618, label = 'Total Price')

    mpl.axhline(0, color='black', lw=1)

    #Set the tick marks
    mpl.xticks(tickMarks, strTs, rotation='vertical')
    #Set y-axis label
    mpl.ylabel('ASK - SOLD | BID - BOUGHT')
    #Add the label in the upper left
    mpl.legend(loc = 'upper left')
    mpl.show()
