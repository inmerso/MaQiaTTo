import sqlite3

db_file = "storage.db"

TableExists="""
DROP TABLE IF EXISTS Dummy_Topic_Data;
"""

TableSchema="""
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

    sqlite3.complete_statement(TableExists)
    cursor.executescript(TableExists)

    sqlite3.complete_statement(TableSchema)
    cursor.executescript(TableSchema)

    cursor.close()
    connection.close()
