

###########################----------------------------------------------------##############################
###########################........ Author: HYELADZIRA JAMES BALAMI............##############################
###########################.........Student_ID: D3914083.......................##############################
###########################----------------------------------------------------##############################


#................................. PHASE 1 - PYTHON AND SQLITE3 DATABASE QUERIES............................#


#imports
import sqlite3
from datetime import datetime, timedelta


# 1.QUERY TO SELECT ALL COUNTRIES
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






# 2.QUERY TO SELECT ALL CITIES
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




# 3.QUERY TO GET THE AVERAGE ANNUAL TEMPERATURE
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





# 4.QUERY TO GET THE AVERAGE SEVEN DAY PRECIPITATION
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





# 5.QUERY TO GET THE AVERAGE MEAN TEMPERATURE
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
        





# 6.QUERY TO GET THE AVERAGE ANNUAL PRECIPITATION
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
       




 
# 7.QUERY TO GET THE MIN/MAX/MEAN TEMPERATURE AND PRECIPITATION
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






# 8.QUERY TO GET THE MIN AND MAX MONTHLY TEMPERATURE
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
       





# 9.QUERY TO GET THE AVERAGE TEMPERATURE BY AGAINST AVERAGE PRECIPITATION FOR SEVEN DAYS
def average_temperature_vs_average_precipitation(connection, city_id, date):
    # Calculate average temperature vs Average Precipitation by city ID.
   
    try:
        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()
       
        # Define the query 
        query = """
            SELECT date, AVG(mean_temp) AS avg_temperature, AVG(precipitation) AS avg_precipitation
            FROM daily_weather_entries
            WHERE city_id = ? AND date BETWEEN DATE(?) AND DATE(?, '+6 days')
            GROUP BY date
            ORDER BY date;
        """

        # Execute the query via the cursor object and display the results to the console.
        result = cursor.execute(query, (city_id, date, date)).fetchall()

        # Iterate over the results and display the results. 
        for row in result:
            print(f"Date: {row['date']}, AVG Temperature: {row['avg_temperature']:.2f}°C, AVG Precipitation: {row['avg_precipitation']:.2f}mm")
        
        return result
    
    except sqlite3.OperationalError as ex:
        print(f"SQL Error: {str(ex)}")






# 10.QUERY TO GET THE SEVEN DAY AVERAGE TEMPERATURE BY CITY
def seven_day_temperature_by_city(connection, city_id, start_date):
    # Calculate the average temperature for each day over a seven-day range starting from the given date of a given city.
   
    try:
        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()
       
       # Calculate the end date for the 7-day range
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = start_date_obj + timedelta(days=6)
        end_date = end_date_obj.strftime("%Y-%m-%d")

        # Define the query
        query = '''
            SELECT dw.date as date, dw.mean_temp as temperature
            FROM cities c
            JOIN daily_weather_entries dw 
            ON c.id = dw.city_id
            WHERE c.id = ? AND dw.date BETWEEN ? AND ?;
        '''

        # Execute the query via the cursor object and display the results to the console.
        result = cursor.execute(query, (city_id, start_date, end_date)).fetchall()

        print(f"Seven Day Temperature for city ID: {city_id} from {start_date} to {end_date}:")
        for row in result:
            print(f"Date: {row['date']},Temperature: {row['temperature']:.2f}")
        return result
    
    except sqlite3.OperationalError as ex:
        print(f"SQL Error: {str(ex)}")







# 11.QUERY TO GET THE SEVEN DAY PRECIPITATION BY CITY
def seven_day_precipitation(connection, city_id, start_date):
    # Calculate the precipitation for each day over a seven-day range starting from the given date of a given city.

    try:
        # Get a cursor object from the database connection that will be used to execute database query.
        cursor = connection.cursor()

        # Calculate the end date for the 7-day range
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = start_date_obj + timedelta(days=6)
        end_date = end_date_obj.strftime("%Y-%m-%d")

        # Define the query
        query = '''
            SELECT dw.date as date, dw.precipitation as precipitation
            FROM cities c
            JOIN daily_weather_entries dw 
            ON c.id = dw.city_id
            WHERE c.id = ? AND dw.date BETWEEN ? AND ?;
        '''

        # Execute the query via the cursor object and display the results to the console.
        result = cursor.execute(query, (city_id, start_date, end_date)).fetchall()

        print(f"Seven Day Precipitation for city ID: {city_id} from {start_date} to {end_date}:")
        for row in result:
            print(f"Date: {row['date']}, Precipitation: {row['precipitation']:.2f}")
        return result

    except sqlite3.OperationalError as ex:
        print(f"SQL Error: {str(ex)}")

