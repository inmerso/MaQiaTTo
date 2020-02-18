#!/usr/bin/env python

import sqlite3

db_file = "storage.db"

dropTable="""
DROP TABLE IF EXISTS Dummy_Topic_Data;
"""

createTable="""
create table Dummy_Topic_Data (
  id integer primary key autoincrement,
  Sensor text,
  Time text,
  Value text
);
"""

if __name__ == "__main__":

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    sqlite3.complete_statement(dropTable)
    cursor.executescript(dropTable)

    sqlite3.complete_statement(createTable)
    cursor.executescript(createTable)

    cursor.close()
    connection.close()
