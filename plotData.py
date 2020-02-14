import sqlite3
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def convert_time(date_bytes):
    return mdates.strpdate2num(' %d-%b-%Y %H:%M:%S:%f')(date_bytes.decode('ascii'))

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

    datestamp, value = np.loadtxt(graphArray,delimiter=',', unpack=True, converters={ 0: convert_time})

    fig = plt.figure()

    rect = fig.patch

    ax1 = fig.add_subplot(1,1,1)
    plt.plot_date(x=datestamp, y=value, fmt='b-', label = 'value', linewidth=2)
    plt.show()
