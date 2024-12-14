

###########################----------------------------------------------------##############################
###########################........ Author: HYELADZIRA JAMES BALAMI............##############################
###########################.........Student_ID: D3914083.......................##############################
###########################----------------------------------------------------##############################


#................................. PHASE 1 - PYTHON AND SQLITE3 DATABASE QUERIES............................#


#imports
import sqlite3
import pandas as pd
from datetime import datetime, timedelta


def select_all_countries(connection):
    # Queries the database and selects all the countries stored in the countries table of the database.
    # The returned results are then printed to the console.
    try:
        # Define the query
        query = "SELECT * from [countries]"

        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()

        # Execute the query via the cursor object.
        result = cursor.execute(query)

        # Define the columns with column names in the table called countries from the database
        columns = ["id", "name", "timezone"]

        # Creating a dataframe to map it to the columns before iterating
        df = pd.DataFrame(result, columns=columns)
        print(df)

        # Iterate over the results and display the results.
        for _, row in df.iterrows():
            print(f"Country Id: {row['id']} -- Country Name: {row['name']} -- Country Timezone: {row['timezone']}")
            return result
               
    except sqlite3.OperationalError as ex:
        print(ex)





def select_all_cities(connection):
    # Queries the database and selects all the cities stored in the cities table of the database.
    # The returned results are then printed to the console.
    try:
        # Define the query
        query = "SELECT * from [cities]"

        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()

        # Execute the query via the cursor object.
        result = cursor.execute(query)

        # Define the columns with column names in the table called cities from the database
        columns = ["id", "name", "longitude", "latitude", "country_id"]

        # Creating a dataframe to map it to the columns before iterating
        df = pd.DataFrame(result, columns=columns)
        print(df)

        # Iterate over the results and display the results.
        for _, row in df.iterrows():
            print(f"City Id: {row['id']} -- City Name: {row['name']} -- City Longitude: {row['longitude']} -- City Latitude: {row['latitude']} -- City Country_id: {row['country_id']}")
            return result
        
    except sqlite3.OperationalError as ex:
        print(ex)





def average_annual_temperature(connection, city_id, year):
    try:
        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()

        # Define the query
        query = '''
            SELECT AVG(dw.mean_temp)
            FROM cities c
            JOIN daily_weather_entries dw 
            ON c.id = dw.city_id
            WHERE c.id = ? AND strftime('%Y', dw.date) = ?;
        '''

        # Execute the query via the cursor object and display the results to the console.
        result = cursor.execute(query, (city_id, str(year))).fetchone()
        print(f"{result[0]:.2f}")
        return result
    
    except sqlite3.OperationalError as ex:
        print(ex)




def average_seven_day_precipitation(connection, city_id, start_date):
    try:
        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()

        # Calculate the end date for the 7-day range
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = start_date_obj + timedelta(days=6)
        end_date = end_date_obj.strftime("%Y-%m-%d")

        # Define the query
        query = '''
            SELECT AVG(dw.precipitation)
            FROM cities c
            JOIN daily_weather_entries dw 
            ON c.id = dw.city_id
            WHERE c.id = ? AND dw.date BETWEEN ? AND ?;
        '''

        # Execute the query via the cursor object and display the results to the console.
        result = cursor.execute(query, (city_id, start_date, end_date)).fetchone()
        print(f"{result[0]:.2f}")
        return result

    except sqlite3.OperationalError as ex:
        print(ex)





def average_mean_temp_by_city(connection, date_from, date_to):
        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()

        # Define the query 
        query = '''
            SELECT AVG(dw.mean_temp), c.name
            FROM cities c
            JOIN daily_weather_entries dw 
            ON c.id = dw.city_id
            WHERE dw.date BETWEEN ? AND ?
            GROUP BY c.name;
        '''

        # Execute the query via the cursor object and display the results to the console.
        result = cursor.execute(query, (date_from, date_to)).fetchall()

        # Iterate over the results and display the results. 
        for row in result:           print(f"City: {row[0]} -- Avg Temperature: {row[1]}°C")
        return result
        




def average_annual_precipitation_by_country(connection, year):
    # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()

        # Define the query 
        query = '''
            SELECT AVG(dw.precipitation), co.name
            FROM countries co
            JOIN cities c 
            ON co.id = c.country_id
            JOIN daily_weather_entries dw 
            ON c.id = dw.city_id
            WHERE strftime('%Y', dw.date) = ?
            GROUP BY co.name;
        '''

        # Execute the query via the cursor object and display the results to the console.
        result = cursor.execute(query, (year,)).fetchall()

        # Iterate over the results and display the results. 
        for row in result:
            print(f"Country: {row[0]} -- Avg Precipitation: {row[1]:.2f} mm")
        return result





# def select_all_countries2(connection):
#     # Queries the database and selects all the countries stored in the countries table of the database.
#     # The returned results are then printed to the console.
#     try:
#         # Define the query
#         query = "SELECT * from [countries]"

#         # Get a cursor object from the database connection that will be used to execute database query.
#         cursor = connection.cursor()

#         # Execute the query via the cursor object.
#         results = cursor.execute(query)

#         return results
        
#     except sqlite3.OperationalError as ex:
#         raise Exception(f"{str(ex)}")





if __name__ == "__main__":
    with sqlite3.connect("/Users/hyeladzirajames/Library/CloudStorage/OneDrive-TeessideUniversity/SECOND SEMESTER/SOFTWARE FOR DIGITAL INNOVATIONS/ICA_DELIVERABLES/D3914083_JAMES.HYELADZIRA/Historical_Weather-Data_App(Open-Meteo-Weather-Data)/CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as conn:

        select_all_countries(conn)
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

        select_all_cities(conn)
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

        average_annual_temperature(conn, 1, 2021)
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

        average_seven_day_precipitation(conn, 2, "2022-05-16")
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

        average_mean_temp_by_city(conn, "2022-05-19", "2022-05-30")
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

        average_annual_precipitation_by_country(conn, 2021)
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

