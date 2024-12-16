

###########################----------------------------------------------------##############################
###########################........ Author: HYELADZIRA JAMES BALAMI............##############################
###########################.........Student_ID: D3914083.......................##############################
###########################----------------------------------------------------##############################


#................................. PHASE 1 - PYTHON AND SQLITE3 DATABASE QUERIES............................#


#imports
import sqlite3
import os
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

        # Iterate over the results and display the results.
        for row in result:
           print(f"Country Id: {row['id']} -- Country Name: {row['name']} -- Country Timezone: {row['timezone']}")
        return result
               
    except sqlite3.OperationalError as ex:
        print(f"SQL Error: {str(ex)}")






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

        # Iterate over the results and display the results.
        for row in result:

            longitude = float(row['longitude'])
            latitude = float(row['latitude'])

            print(f"City Id: {row['id']} -- City Name: {row['name']} -- City Longitude: {longitude:.2f} -- City Latitude: {latitude:.2f} -- City Country_id: {row['country_id']}")
        
            
        return result
        
    except sqlite3.OperationalError as ex:
        print(f"SQL Error: {str(ex)}")




def average_annual_temperature(connection, city_id, year):
    # Calculate the average annual temperature for a given city and year.

    try:
        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()

        # Define the query
        query = '''
            SELECT c.name as city_name, AVG(dw.mean_temp) as avg_mean_temp
            FROM cities c
            JOIN daily_weather_entries dw 
            ON c.id = dw.city_id
            WHERE c.id = ? AND strftime('%Y', dw.date) = ?;
        '''

        # Execute the query via the cursor object and display the results to the console.
        result = cursor.execute(query, (city_id, year)).fetchone()

        print(f"Average annual temperature for city Id {city_id} and City Name {result['city_name']} in {year}: {result['avg_mean_temp']:.2f}°C")

        return result
    
    except sqlite3.OperationalError as ex:
         print(f"SQL Error: {str(ex)}")




def average_seven_day_precipitation(connection, city_id, start_date):
    # Calculate the average seven day precipitation from a given start date for a given city.

    try:
        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()

        # Calculate the end date for the 7-day range
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = start_date_obj + timedelta(days=6)
        end_date = end_date_obj.strftime("%Y-%m-%d")

        # Define the query
        query = '''
            SELECT AVG(dw.precipitation) as avg_precipitation
            FROM cities c
            JOIN daily_weather_entries dw 
            ON c.id = dw.city_id
            WHERE c.id = ? AND dw.date BETWEEN ? AND ?;
        '''

        # Execute the query via the cursor object and display the results to the console.
        result = cursor.execute(query, (city_id, start_date, end_date)).fetchone()
        print(f"Average Seven Day Precipitation for city ID: {city_id} from date {start_date} to date {end_date} is: {result['avg_precipitation']:.2f}mm")
        return result

    except sqlite3.OperationalError as ex:
        print(f"SQL Error: {str(ex)}")





def average_mean_temp_by_city(connection, date_from, date_to):
    # Calculate the average mean temperature for a given between given dates.

    try:
        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()

        # Define the query 
        query = '''
            SELECT c.name as city_name, AVG(dw.mean_temp) as avg_mean_temp
            FROM cities c
            JOIN daily_weather_entries dw 
            ON c.id = dw.city_id
            WHERE dw.date BETWEEN ? AND ?
            GROUP BY c.id;
        '''

        # Execute the query via the cursor object and display the results to the console.
        result = cursor.execute(query, (date_from, date_to)).fetchall()

        # Iterate over the results and display the results. 
        for row in result:
            #print(dict(row))      
            print(f"City: {row['city_name']} -- Avg Temperature: {row['avg_mean_temp']:.2f}°C")
        return result
    
    except sqlite3.OperationalError as ex:
        print(f"SQL Error: {str(ex)}")
        




def average_annual_precipitation_by_country(connection, year):
   # Calculate the average annual precipitation by a given country and year.

    try:
         # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()

        # Define the query 
        query = '''
            SELECT co.name as country_name, AVG(dw.precipitation) as avg_precipitation
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
            Country = (row['country_name'])
            Avg_Precipitation = float(row['avg_precipitation'])
            print(f"Country: {Country} -- Avg_Precipitation: {Avg_Precipitation:.2f} mm")
        return result
    
    except sqlite3.OperationalError as ex:
        print(f"SQL Error: {str(ex)}")
       





def min_max_mean_temperature_and_precipitation_by_city(connection, year):
    # Calculate the min/max/mean temperature and precipitation for a given city and year.

    try:
        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()

        # Define the query 
        query = '''
            SELECT c.name as city_name,
                MIN(dw.min_temp) as min_temperature,
                MAX(dw.max_temp) as max_temperature,
                AVG(dw.mean_temp) as mean_temperature,
                MIN(dw.precipitation) as min_precipitation,
                MAX(dw.precipitation) as max_precipitation,
                AVG(dw.precipitation) as mean_precipitation
            FROM cities c
            JOIN daily_weather_entries dw
            ON c.id = dw.city_id
            WHERE strftime('%Y', dw.date) = ?
            GROUP BY c.name;
        '''

        # Execute the query via the cursor object and display the results to the console.
        result = cursor.execute(query, (year,)).fetchall()

        # Iterate over the results and display the results. 
        for row in result:

            print(f"City: {row['city_name']} -- Min Temperature: {row['min_temperature']:.2f}°C, Max Temperature: {row['max_temperature']:.2f}°C, Mean Temperature: {row['mean_temperature']:.2f}°C")
            print(f"City: {row['city_name']} -- Min Precipitation: {row['min_precipitation']:.2f}°C, Max Precipitation: {row['max_precipitation']:.2f}°C, Mean Precipitation: {row['mean_precipitation']:.2f}°C")
            
        return result
    
    except sqlite3.OperationalError as ex:
        print(f"SQL Error: {str(ex)}")





def minimum_and_maximum_monthly_temperature_by_city(connection, city_id, year):
    # Calculate the minimum and maximum monthly temperature for a given city and year.
   
    try:
        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()
       
        # Define the query 
        query = '''
            SELECT strftime('%m', dw.date) as month, MIN(dw.min_temp) as min_temperature, MAX(dw.max_temp) as max_temperature
            FROM cities c
            JOIN daily_weather_entries dw
            ON c.id = dw.city_id
            WHERE c.id = ?
            AND strftime('%Y', dw.date) = ?
            GROUP BY month
            ORDER BY month;
        '''

        # Execute the query via the cursor object and display the results to the console.
        result = cursor.execute(query, (city_id, year)).fetchall()

        # Iterate over the results and display the results. 
        for row in result:
            print(f"Month: {row['month']} -- Min Temperature: {row['min_temperature']:.2f}°C, Max Temperature: {row['max_temperature']:.2f}°C")
            
        return result
    
    except sqlite3.OperationalError as ex:
        print(f"SQL Error: {str(ex)}")
       




def average_temperature_by_city_and_country(connection, city_id, year):
    # Calculate average temperature by city and country in a given year.
   
    try:
        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()
       
        # Define the query 
        query = '''
            SELECT c.name as city_name, co.name as country_name, AVG(dw.min_temp) as avg_temperature
            FROM cities c
            JOIN countries co
            ON c.country_id = co.id
            JOIN daily_weather_entries dw
            ON c.id = dw.city_id
            WHERE c.id = ? 
            AND strftime('%Y', dw.date) = ? 
            GROUP BY c.name, co.name;
        '''

        # Execute the query via the cursor object and display the results to the console.
        result = cursor.execute(query, (city_id, year)).fetchall()

        # Iterate over the results and display the results. 
        for row in result:
            print(f"Country: {row['country_name']} -- City: {row['city_name']}°C, AVG Min Temperature: {row['avg_temperature']:.2f}°C")
            
        return result
    
    except sqlite3.OperationalError as ex:
        print(f"SQL Error: {str(ex)}")






def average_rainfall_by_city_and_country(connection, city_id, year):
    # Calculate average rainfall by city and country in a given year.
   
    try:
        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()
       
        # Define the query 
        query = '''
            
        '''

        # Execute the query via the cursor object and display the results to the console.
        result = cursor.execute(query, (city_id, year)).fetchall()

        # Iterate over the results and display the results. 
        for row in result:
            print(f"Country: {row['country_name']} -- City: {row['city_name']}°C, AVG Rainfall: {row['avg_rainfall']:.2f}°C")
            
        return result
    
    except sqlite3.OperationalError as ex:
        print(f"SQL Error: {str(ex)}")







file_path = os.path.abspath(__file__)
working_directory = os.path.dirname(file_path)
os.chdir(working_directory)
database_location = "CIS4044-N-SDI-OPENMETEO-PARTIAL.db"

if __name__ == "__main__":

    with sqlite3.connect(database_location) as conn:
        conn.row_factory = sqlite3.Row
        
        print("------------Select All Countries--------------------------------------------------------------------------------")
        select_all_countries(conn)
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

        print("------------Select All Cities-----------------------------------------------------------------------------------")
        select_all_cities(conn)
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

        print("------------Average Annual Temperature--------------------------------------------------------------------------")
        average_annual_temperature(conn, 1, "2021")
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

        print("------------Average Seven Day Precipitation---------------------------------------------------------------------")
        average_seven_day_precipitation(conn, 2, "2022-05-16")
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

        print("------------Average Mean Temperature By City--------------------------------------------------------------------")
        average_mean_temp_by_city(conn, "2022-05-19", "2022-05-30")  
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

        print("------------Average Annual Precipitation By Country-------------------------------------------------------------")
        average_annual_precipitation_by_country(conn, "2020")
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

        print("------------Min, Max and Mean Temperature and Precipitation By City---------------------------------------------")
        min_max_mean_temperature_and_precipitation_by_city(conn, "2021")
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

        print("------------Minimum and Maximum Monthly Temperature By City-----------------------------------------------------")
        minimum_and_maximum_monthly_temperature_by_city(conn, 2, "2021")
        print("----------------------------------------------------------------------------------------------------------------")
        print("\n")

        print("------------Average Temperature By City And Country------------------------------------------------------------")
        average_temperature_by_city_and_country(conn, 1, "2022")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\n")

        print("------------Average Rainfall By City And Country---------------------------------------------------------------")
        average_rainfall_by_city_and_country(conn, 1, "2022")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\n")

