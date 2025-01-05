

###########################----------------------------------------------------##############################
###########################........ Author: HYELADZIRA JAMES BALAMI............##############################
###########################.........Student_ID: D3914083.......................##############################
###########################----------------------------------------------------##############################


#................................. PHASE 3 - DATA RETRIEVAL AND STORAGE............................#

# IMPORTS
import sqlite3
import requests
import os



def data_retrieval_and_storage():
    # Getting the parameters for the API request
    params = {
        "latitude" : 51.50853,
        "longitude" : -0.12574,
        "daily" : [ "temperature_2m_max", "temperature_2m_min", "precipitation_sum", "temperature_2m_mean" ],
        "timezone" : "Europe/London",
        "start_date" : "2023-01-01",
        "end_date" : "2024-11-30",  
    }

    try: 
        # API request
        # Fetching data from Open Meteo API
        response = requests.get ( "https://archive-api.open-meteo.com/v1/archive", params ) 
        result = response.json( )
        daily_weather_result = result.get("daily")

        # Extracting the data
        days = daily_weather_result["time"]
        max_temp = daily_weather_result["temperature_2m_max"]
        min_temp = daily_weather_result["temperature_2m_min"]
        mean_temp = daily_weather_result["temperature_2m_mean"]
        precipitation  = daily_weather_result["precipitation_sum"]

        # Preparing the data for insertion into SQLite
        daily_weather_objects = []
        for index,day in enumerate(days):
            weather_object = {
                "mean_temp" : mean_temp[index], 
                "min_temp" : min_temp[index],
                "max_temp" : max_temp[index],
                "mean_temp" : mean_temp[index],
                "precipitation" : precipitation[index],
                "date" : day,
                "city_id" : 2,
            }
            daily_weather_objects.append(weather_object)
            
        # Set the working directory
        file_path = os.path.abspath(__file__)
        working_directory = os.path.dirname(file_path)
        os.chdir(working_directory)
        database_location = "CIS4044-N-SDI-OPENMETEO-PARTIAL.db"

        # Inserting the data into SQLite")
        for data in daily_weather_objects:
            values = tuple (data.values())
            print (values)
            query = '''
                    INSERT INTO daily_weather_entries (mean_temp, min_temp, max_temp, precipitation, date, city_id) 
                    values (?,?,?,?,?,?)
                '''
            with sqlite3.connect(database_location) as conn:
             cursor = conn.cursor()
             cursor.execute(query, values )

            print("Data retrieval and storage completed successfully!")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Open Meteo API: {e}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


