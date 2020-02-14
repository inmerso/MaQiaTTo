import json
import sqlite3
from datetime import datetime

dbFileName = "storage.db"

class DatabaseHandler():
    def __init__(self):
        self.conn = sqlite3.connect(dbFileName)
        self.conn.execute('pragma foreing_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def add_entry(self, sql_query, args=()):
        self.cur.execute(sql_query, args)
        self.conn.commit()
        return

    def __del__(self):
        self.cur.close()
        self.conn.close()


def DummyTopicDataHandler(data):
    json_d = json.loads(data)

    sensor = json_d['Sensor']
    time = json_d['Time']
    value = json_d['Value']

    dbObj = DatabaseHandler()
    dbObj.add_entry("insert into Dummy_Topic_Data (Sensor, Time, Value) values (?,?,?)", [sensor, time, value])
    del dbObj

    print("Entry added")


def db_add(topic, data_json):
    if topic == "DummyTopic":
        DummyTopicDataHandler(data_json)
