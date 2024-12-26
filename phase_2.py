

###########################----------------------------------------------------##############################
###########################........ Author: HYELADZIRA JAMES BALAMI............##############################
###########################.........Student_ID: D3914083.......................##############################
###########################----------------------------------------------------##############################


#................................. PHASE 2 - PBASIC GRAPH PLOTS USING MATPLOTLIB LIBRARY............................#



# Imports
import sqlite3
import os
import matplotlib as plt
from phase_1 import ( 
    min_max_mean_temperature_and_precipitation_by_city, 
    seven_day_temperature_by_city, 
    seven_day_precipitation, 
    minimum_and_maximum_monthly_temperature_by_city, 
    average_mean_temp_by_city, )


# PLOT ALL THE CHARTS IN A BLOCK CALLED WEATHER DATA APP

def plot_open_meteo_weather_data_app(connection, city_id):
     
   # 1. Bar Chart To Show The Seven Day Precipitation

      data = seven_day_precipitation(connection, city_id, "2022-01-16")
      dates = [row[0] for row in data]
      precipitation = [row[1] for row in data]

      # plot the bar graph
      plt.subplot(3, 2, 1)
      plt.bar(dates, precipitation, color='blue', label='Precipitation (mm)')

      # add the x and y labels and the bar graph title 
      plt.xlabel("Date")
      plt.ylabel("Precipitation (mm) ")
      plt.title(f"SEVEN DAY PRECIPITATION FOR CITY 1D {city_id}" )
      plt.xticks(rotation=50)
      plt.legend()
      


   # 2. Bar Chart To Show The Average Seven Temperature For a Set of Cities
 
      data = average_mean_temp_by_city(connection)
      cities = [row[0] for row in data]
      avg_temp = [row[1] for row in data]

      # plot the bar graph
      plt.subplot(3, 2, 2)
      plt.bar(cities, avg_temp, color='green', label='Average Temperature')

      # add the x and y labels and the bar graph title 
      plt.xlabel("Cities")
      plt.ylabel("Average Temperature ")
      plt.title("AVERAGE TEMPERATURE FOR A SET OF CITIES " )
      plt.xticks(rotation=50)
      plt.legend()   
    


   # 3. Line Chart To Show The Seven Day Average Temperature Variation

      data = seven_day_temperature_by_city(connection, city_id)
      days = [row[0] for row in data]
      avg_temp = [row[1] for row in data]

      # plot the line chart
      plt.subplot(3, 2, 3)
      plt.plot(days, avg_temp, color='red', marker='o', label='Precipitation (mm)')

      # add the x and y labels and the bar graph title 
      plt.xlabel("Days")
      plt.ylabel("Temperature ")
      plt.title(f"SEVEN DAY AVERAGE TEMPERATURE VARIATION FOR CITY ID {city_id} " )
      plt.xticks(rotation=50)



   # 4.Grouped Bar Chart to Show The Min/Max/Mean Temperature and precipitation

      data = min_max_mean_temperature_and_precipitation_by_city(connection, city_id)
      cities = [row['city_name'] for row in data]
      min_temp = [row['min_temperature'] for row in data]
      max_temp = [row['max_temperature'] for row in data]
      mean_temp = [row['mean_temperature'] for row in data]
      min_precip = [row['min_precipitation'] for row in data]
      max_precip = [row['max_precipitation'] for row in data]
      mean_precip = [row['mean_precipitation'] for row in data]

      # Set up the positions for the bars
      x = range(len(cities))
      width = 0.15 

      # Plot the grouped bar charts
      plt.subplot(3, 2, 4)
      #fig, ax = plt.subplots(figsize=(10, 6))

      plt.bar(x, min_temp, width=0.2, label='Min Temp', align='center')
      plt.bar([p + 0.2 for p in x], max_temp, width=0.2, label='Max Temp', align='center')
      plt.bar([p + 0.4 for p in x], mean_temp, width=0.2, label='Mean Temp', align='center')
      plt.bar([i - width for i in x], min_precip, width=width, label='Min Precip (mm)', bottom=min_temp, color='lightblue')
      plt.bar(x, max_precip, width=width, label='Max Precip (mm)', bottom=max_temp, color='pink')
      plt.bar([i + width for i in x], mean_precip, width=width, label='Avg Precip (mm)', bottom=mean_temp, color='lightgreen')

      # Add labels and title
      plt.xlabel('City')
      plt.ylabel('Temperature (°C) / Precipitation (mm)')
      plt.title(f" Weather Data for Cities ")
      plt.xticks([p + 0.2 for p in x], cities)
      plt.legend()



   # 5. MULTI-LINE CHART TO SHOW THE MINIMUM AND MAXIMUM TEMPERATURE FOR 12 months

      data = minimum_and_maximum_monthly_temperature_by_city(connection, city_id)
      months = [row[0] for row in data]
      min_temp = [row[1] for row in data]
      max_temp = [row[2] for row in data]

      # Plot the multi-line chart
      plt.subplot(3, 2, 5)
      plt.plot(months, min_temp, label='Min Temperature (°C)', color='blue', marker='o')
      plt.plot(months, max_temp, label='Max Temperature (°C)', color='red', marker='o')

      # add the x and y labels and the bar graph title 
      plt.xlabel("Months")
      plt.ylabel("Temperature (°C)")
      plt.title(f"DAILY MINIMUM AND MAXIMUM TEMPERATURE FOR CITY ID {city_id} " )
      plt.xticks(rotation=50)
      plt.legend()
      plt.grid(True, linestyle='--', alpha=0.7)



   # 6. SCATTER PLOT CHART TO SHOW THE AVERAGE TEMPERATURE AGAINST AVERAGE RAINFALL FOR A GIVEN CITY/COUNTRY.

      # temperature_data = queries.average_temperature_by_city_and_country(connection, city_id, year)
      # rainfall_data = queries.average_rainfall_by_city_and_country(connection, city_id, year)
      
      # # Plot the Scatterplot chart
      # plt.scatter(temperature_data, rainfall_data, color='blue', label='City Data')

      # # add the x and y labels and the bar graph title 
      # plt.xlabel("Average Temperature (°C) ")
      # plt.ylabel("Average Rainfall (mm)")
      # plt.title(f"AVERAGE TEMPERATURE AGAINST AVERAGE RAINFALL FOR CITY ID {city_id} IN THE YEAR {year} " )
      # plt.legend()
      # plt.grid(True, linestyle='--', alpha=0.7)


  # DISPLAY ALL CHARTS
      plt.tight_layout() 
      plt.show()

# Function to retrieve country_id and city_id based on user input
def get_city_and_country_ids(connection, country_name, city_name):
    query = """
    SELECT countries.id AS country_id, cities.id AS city_id
    FROM countries
    JOIN cities ON countries.id = cities.country_id
    WHERE countries.name = ? AND cities.name = ?
    """
    cursor = connection.cursor()
    cursor.execute(query, (country_name, city_name))
    result = cursor.fetchone()
    return result if result else (None, None)


file_path = os.path.abspath(__file__)
working_directory = os.path.dirname(file_path)
os.chdir(working_directory)
#database_location = "CIS4044-N-SDI-OPENMETEO-PARTIAL.db"

if __name__ == "__main__":
    database_location = "CIS4044-N-SDI-OPENMETEO-PARTIAL.db"
    with sqlite3.connect(database_location) as conn:
      conn.row_factory = sqlite3.Row
      while True:
        country = input("Enter country (or press 'x' to exit): ").strip()
        if country.lower() == 'x':
            print("Exiting the application.")
            break
        city = input("Enter city: ").strip()
        country_id, city_id = get_city_and_country_ids(conn, country, city)

        if not country_id or not city_id:
                print("Error: Invalid country or city. Please try again.")
                continue

        try:
                plot_open_meteo_weather_data_app(conn, country_id, city_id)
        except Exception as e:
                print(f"An error occurred while plotting data: {e}")
        

      
     