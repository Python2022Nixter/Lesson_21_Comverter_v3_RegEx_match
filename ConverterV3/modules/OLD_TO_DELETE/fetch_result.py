import sqlite3
import pathlib

FILE_NAME = "db1.db"
DB_FOLDER = "DB1"
TABLE_NAME = "employees"
PATH_TO_FILE = pathlib.Path(__file__).parent.joinpath(DB_FOLDER, FILE_NAME)

SQL_CREATE_TABLE = F"""
CREATE TABLE "{TABLE_NAME}" (
	"id"	INTEGER  UNIQUE,
	"department_name"	TEXT,
	"manager_id"	INTEGER,
	"description"	TEXT,
	PRIMARY KEY("id")
);


"""

SQL_GET_ALL_RECORDS = F"SELECT * FROM '{TABLE_NAME}';"

with sqlite3.connect(PATH_TO_FILE) as c:
    cursor = c.cursor()
    cursor.execute(SQL_GET_ALL_RECORDS)
    res = cursor.fetchall()
    pass

print (type(res))
print (len(res))
print (res[0])
print (res[0][3])
