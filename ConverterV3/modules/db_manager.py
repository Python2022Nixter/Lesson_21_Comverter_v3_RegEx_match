import json
import os
import pathlib
import sqlite3
import modules.constants as CONST
import requests
# pip install requests

# Create tables
def create_table_rates():
    with sqlite3.connect(CONST.PATH_TO_DB) as c:
        cursor = c.cursor()
        cursor.execute(CONST.SQL_CREATE_TABLE_RATES)
        pass
    pass

def create_table_countries():
    with sqlite3.connect(CONST.PATH_TO_DB) as c:
        cursor = c.cursor()
        cursor.execute(CONST.SQL_CREATE_TABLE_COUNTRIES)
        pass

    pass

def create_table_conversions():
    with sqlite3.connect(CONST.PATH_TO_DB) as c:
        cursor = c.cursor()
        cursor.execute(CONST.SQL_CREATE_TABLE_CONVERSIONS)
    pass

    pass

# Drop tables
def drop_rates_from_database():
    with sqlite3.connect(CONST.PATH_TO_DB) as c:
        try:
            cursor = c.cursor()
            cursor.execute(F"DROP TABLE IF EXISTS {CONST.TABLE_RATES} ")
            pass
        except sqlite3.IntegrityError as e:
            print(e.__annotations__)
            pass
        pass
    pass

def drop_countries_from_database():
    with sqlite3.connect(CONST.PATH_TO_DB) as c:
        try:
            cursor = c.cursor()
            cursor.execute(F"DROP TABLE IF EXISTS  {CONST.TABLE_COUNTRIES} ")
            pass
        except sqlite3.IntegrityError as e:
            print(e.__annotations__)
            pass
        pass
    pass

def drop_conversions_from_database():
    with sqlite3.connect(CONST.PATH_TO_DB) as c:
        try:
            cursor = c.cursor()
            cursor.execute(F"DROP TABLE IF EXISTS  {CONST.TABLE_CONVERSIONS_HISTORY} ")
            pass
        except sqlite3.IntegrityError as e:
            print(e.__annotations__)
            pass
        pass
    pass

# Import from JSON to DB

def import_rates_from_json( file_path = CONST.PATH_TO_RATES_JSON):
    with open(file_path) as f:
        json_data = json.load(f)
        pass
    rates_to_write = [ [item[0], item[1], json_data['date'] ] for item  in json_data['rates'].items() ]
    with sqlite3.connect(CONST.PATH_TO_DB) as c:
        try:
            cursor = c.cursor()
            cursor.executemany(CONST.SQL_POPULATE_TABLE_RATES, rates_to_write)
            pass
        except sqlite3.IntegrityError as e:
            print(e.__annotations__)
            pass
        pass
    pass

# Control / correct incorrect data in JSON - countries
err_fields_counter = 0
def check_key(dictionary_to_check, key):
    global err_fields_counter
    if list(dictionary_to_check.keys()).count(key) != 0: return dictionary_to_check[key]
    else: 
        err_fields_counter += 1
        return "NO_DATA_" + str(err_fields_counter)

def import_countries_from_json():

    with open(CONST.PATH_TO_COUNTRIES_JSON) as f:
        json_data = json.load(f)
        pass
    
    countries_to_write = []
    for next_country in json_data:
        countries_to_write.append(
            [
                check_key(next_country, "continent_name"),
                check_key(next_country, "country_code"),
                check_key(next_country, "country_name"),
                check_key(next_country, "continent_code"),
                check_key(next_country, "capital_name"),
                check_key(next_country, "currency_code"),
                check_key(next_country, "phone_code"),
                check_key(next_country, "three_letter_country_code")
            ]
            )
        pass
    
    print (type(countries_to_write))
    for c in countries_to_write:
        print (len(c))
    with sqlite3.connect(CONST.PATH_TO_DB) as c:
        c.set_trace_callback(print)
        try:
            cursor = c.cursor()
            cursor.executemany(CONST.SQL_POPULATE_TABLE_COUNTRIES, countries_to_write)
            pass
        except sqlite3.Error as e:
            print(e.__annotations__)
            pass
        pass
    pass


# Import from internet to DB (renew database from internet)
def get_rates_online():
    # STEP1 : send HTTP request
    # print (CONST.RATES_URL)
    response = requests.get(CONST.RATES_URL)
    # print(response.json())
    print("response.status_code: " , response.status_code)
    """
    Informational responses (100–199)
    Successful responses (200–299)
    Redirection messages (300–399)
    Client error responses (400–499)
    Server error responses (500–599)
    """
    if int(response.status_code) not in range(200, 300): 
        print ("Response ERROR")
        return False

    # STEP2 : create new JSON file (if file date older)
    ## get directory listing, check files creation dates
    current_date_suffix = response.json()["date"].replace("-", "_") + ".json"
    # print(current_date_suffix)
    for next_path in os.listdir(CONST.PATH_TO_JSON):        
        if next_path.endswith(current_date_suffix): 
            print ("Rates file for this date exists already")
            return False
        pass
    ## save response data to JSON file
    new_file_path = pathlib.Path(CONST.PATH_TO_JSON).joinpath("exchange_" +  current_date_suffix )    
    with open(new_file_path, "w") as f:
        json.dump(response.json(), f)
        pass 

    # STEP3 : drop old table from database
    drop_rates_from_database()

    # STEP4 : create new table with current rates data
    create_table_rates()
    import_rates_from_json(file_path = new_file_path)    

    return True

# Print tables (to console, to file, send to email)  tables: rates, countries, conversions
def print_reports(table_headers: list, table_rows: list):
    table_to_print = ""
    for col_head in table_headers:
        # print headers
        table_to_print += F"{col_head:<20s} | "
        pass

    table_to_print += "\n"
    table_to_print += (20 + 3) * len(table_headers) * "_" + "\n"
    for next_row in table_rows:
        for col_data in next_row:
            table_to_print += F"{col_data:<20s} | "
            pass
        table_to_print += "\n"       

        pass
    with open("test_report.txt" , "w") as f:
        print(print_reports, file = f)
        pass

    return table_to_print


# get currency code from console ( by country code, country name, tel code, currency code)

def get_curency_code():
    code = None
    # STEP 1 : get currency code from console
    
    menu_string = ""
    
    for i in range(len(CONST.COUNTRY_PROPERTIES)):
        menu_string += F"{i+1} - {CONST.COUNTRY_PROPERTIES[i]}\n"
        pass
    menu_string += ": "
    search_key = input(menu_string)
    print(search_key, CONST.COUNTRY_PROPERTIES[int(search_key)-1])
    search_value = input("Enter search value: ")
    print(CONST.COUNTRY_PROPERTIES[int(search_key)-1],search_value)
    
    # STEP 2 : search in DB
    with sqlite3.connect(CONST.PATH_TO_DB) as c:
        cursor = c.cursor()
        cursor.execute(CONST.SQL_GET_COUNTRY.replace("key", CONST.COUNTRY_PROPERTIES[int(search_key)-1]).replace("value", search_value))
        res = cursor.fetchall()
        print(res)
        pass
    
    
    # STEP 3 :  return currency code
    
    pass
