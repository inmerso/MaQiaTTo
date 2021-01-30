#!/usr/bin/env python

import sqlite3
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def convert_time(date_bytes):
    data_date = datetime.strptime(date_bytes.decode('utf-8'), ' %d-%b-%Y %H:%M:%S:%f')
    data_num = mdates.date2num( data_date )
    return data_num

if __name__ == "__main__":
    conn = sqlite3.connect("storage.db")
    curs = conn.cursor()
    sql_query = "select * from Dummy_Topic_Data"

    graphArray = []

    for row in curs.execute(sql_query):
        info = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
        splitInfo = info.split(',')

        coordinates = splitInfo[2] + ',' + splitInfo[3]
        graphArray.append(coordinates)

    if len(graphArray) == 0:
        print("No data present!")
        exit(1)
    
    datestamp, value = np.loadtxt(graphArray,
                                  delimiter=',',
                                  unpack=True,
                                  converters={ 0: convert_time})

    fig = plt.figure()

    rect = fig.patch

    ax1 = fig.add_subplot(1,1,1)
    plt.plot_date(x=datestamp, y=value, fmt='b-', label = 'value', linewidth=2)
    plt.show()
