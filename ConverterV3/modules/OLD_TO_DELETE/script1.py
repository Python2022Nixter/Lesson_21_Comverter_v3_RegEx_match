import sqlite3
import pathlib

FILE_NAME = "db1.db"
DB_FOLDER = "DB1"
TABLE_NAME = "test222"
PATH_TO_FILE = pathlib.Path(__file__).parent.joinpath(DB_FOLDER, FILE_NAME)

"""

"""

SQL_CREATE_TABLE = F"""
CREATE TABLE "{TABLE_NAME}" (
	"id"	INTEGER  UNIQUE,
	"department_name"	TEXT,
	"manager_id"	INTEGER,
	"description"	TEXT,
	PRIMARY KEY("id")
);


"""

with sqlite3.connect(PATH_TO_FILE) as c:
    cursor = c.cursor()
    cursor.execute(SQL_CREATE_TABLE)
    pass

