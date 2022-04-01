import json
import sqlite3

def create_table_from_json(jsonFile, dbFile):
    # STEP1: read file
    with open(jsonFile) as f:
        json_data = json.load(f)
        pass
    date_to_write = json_data['date']   
    rates_to_write =  json_data['rates'].items() # convert dictionary to tuple of key - value pairs

    # STEP2: create table
    SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS "rates" (
        "code"	TEXT NOT NULL UNIQUE,
        "rate_to_euro" REAL,
        "date"	TEXT,
        PRIMARY KEY("code")
    );
    """ 

    with sqlite3.connect(dbFile) as c:
        cursor = c.cursor()
        cursor.execute(SQL_CREATE_TABLE)
        pass

    # STEP3: populate table rates
    ## STEP3_1: create query
    SQL_POPULATE_TABLE = F"""
    INSERT INTO "rates" ("code", "rate_to_euro", "date")
    values 
    (?, ?, DATE (" {date_to_write} "))

    """ 
    # print(SQL_POPULATE_TABLE)
    ## STEP3_2: issue query
    with sqlite3.connect(dbFile) as c:
        try:
            cursor = c.cursor()
            cursor.executemany(SQL_POPULATE_TABLE, rates_to_write) 
            pass
        except sqlite3.IntegrityError as e:
            print(e.__annotations__)
            pass
        pass

    pass # Function END

def convert(from_currency, to_currency, amnt, dbFile ):
    converted_amount = None
    # Query database:
    QUERY_FROM = F"""
        SELECT rate_to_euro FROM rates
        WHERE code = "{from_currency}" 
    """ 
    QUERY_TO = F"""
        SELECT rate_to_euro FROM rates
        WHERE code = "{to_currency}" 
    """
     
    with sqlite3.connect(dbFile) as c:
        try:
            cursor = c.cursor()
            cursor.execute(QUERY_FROM)
            from_rate = cursor.fetchone()[0]
            cursor.execute(QUERY_TO)
            to_rate = cursor.fetchone()[0]            
            pass
        except sqlite3.IntegrityError as e:
            print(e.__annotations__)
            pass
        pass
 
    return amnt *  to_rate  / from_rate

# create_table_from_json("exchange.json", "exchange.db")

print (F"Res: {convert('ILS', 'EUR', 1000, 'exchange.db'):10.2f}")