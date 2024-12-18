

#----------------------------------------------------#
#........ Author: HYELADZIRA JAMES BALAMI...........
#.........Student_ID: D3914083......................
#----------------------------------------------------#





# PHASE 2 - BASIC GRAPHS USING MATPLOTLIB LIBRARY


# Imports
import sqlite3
import os
import matplotlib as plt
import matplotlib.pyplot as plt
import phase_1 as queries




# 1.BAR CHART TO SHOW THE SEVEN DAY PRECIPITATION FOR A SPECIFIC CITY
def plot_seven_day_precipitation_bar_chart(connection, city_id, start_date):
  
    try:

      connection.row_factory = sqlite3.Row
      data = queries.seven_day_precipitation(connection, city_id, start_date)
      dates = [row[0] for row in data]
      precipitation = [row[1] for row in data]

      # plot the bar graph
      plt.bar(dates, precipitation, color='blue', label='Precipitation (mm)')

      # add the x and y labels and the bar graph title 
      plt.xlabel("Date")
      plt.ylabel("Precipitation (mm) ")
      plt.title(f"SEVEN DAY PRECIPITATION FOR CITY 1D {city_id} FROM START DATE {start_date}" )
      plt.xticks(rotation=50)

      # show the graph
      plt.tight_layout() 
      plt.show()

    except Exception as ex:
        print(f"Error while plotting bar chart: {str(ex)}")







# 2.BAR CHART TO SHOW THE AVERAGE ANNUAL TEMPERATURE FOR A SET OF CITIES
def plot_specific_period_bar_chart(connection):
  
    try:

      connection.row_factory = sqlite3.Row
      data = queries.select_all_cities(connection)
      cities = [row[0] for row in data]
      longitude = [row[1] for row in data]

      # plot the bar graph
      plt.bar(cities, longitude, color='green', label='Longitude')

      # add the x and y labels and the bar graph title 
      plt.xlabel("City")
      plt.ylabel("Longitude ")
      plt.title("LONGITUDINAL VALUE FOR A SET OF CITIES " )
      plt.xticks(rotation=50)

      # show the graph
      plt.tight_layout() 
      plt.show()

    except Exception as ex:
        print(f"Error while plotting bar chart: {str(ex)}")
    
    



# 3.BAR CHART TO SHOW THE AVERAGE YEARLY PRECIPITATION BY COUNTRY
def plot_average_yearly_precipitation_bar_chart(connection, year):
  
    try:

      connection.row_factory = sqlite3.Row
      data = queries.average_annual_precipitation_by_country(connection, year)
      country = [row[0] for row in data]
      avg_precipitation = [row[1] for row in data]

      # plot the bar graph
      plt.figure(figsize = (10,6) )
      plt.bar(country, avg_precipitation, color='green', label='Precipitation (mm)')

      # add the x and y labels and the bar graph title 
      plt.xlabel("Country")
      plt.ylabel("Average Yearly Precipitation (mm)")
      plt.title(f"AVERAGE YEARLY PRECIPITATION BY COUNTRY IN THE YEAR {year} " )
      plt.xticks(rotation=50)

      # show the graph
      plt.tight_layout() 
      plt.show()

    except Exception as ex:
        print(f"Error while plotting bar chart: {str(ex)}")







# 4.GROUPED BAR CHARTS TO SHOW THE MIN/MAX/MEAN TEMPERATURE AND PRECIPITATION VALUES FOR SELECTED CITIES.
def plot_grouped_temperature_and_precipitation_bar_chart(connection, year):
  
    try:

      connection.row_factory = sqlite3.Row
      data = queries.min_max_mean_temperature_and_precipitation_by_city(connection, year)
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
      fig, ax = plt.subplots(figsize=(10, 6))

      ax.bar([i - width for i in x], min_temp, width=width, label='Min Temp (°C)', color='blue')
      ax.bar(x, max_temp, width=width, label='Max Temp (°C)', color='red')
      ax.bar([i + width for i in x], mean_temp, width=width, label='Avg Temp (°C)', color='green')

      ax.bar([i - width for i in x], min_precip, width=width, label='Min Precip (mm)', bottom=min_temp, color='lightblue')
      ax.bar(x, max_precip, width=width, label='Max Precip (mm)', bottom=max_temp, color='pink')
      ax.bar([i + width for i in x], mean_precip, width=width, label='Avg Precip (mm)', bottom=mean_temp, color='lightgreen')

        # Add labels and title
      ax.set_xlabel('City')
      ax.set_ylabel('Temperature (°C) / Precipitation (mm)')
      ax.set_title(f"Weather Data for Cities in the year {year}")
      ax.set_xticks(x)
      ax.set_xticklabels(cities, rotation=45, ha='right')

        # Add a legend
      ax.legend()


      # show the graph
      plt.tight_layout() 
      plt.show()

    except Exception as ex:
        print(f"Error while plotting bar chart: {str(ex)}")







file_path = os.path.abspath(__file__)
working_directory = os.path.dirname(file_path)
os.chdir(working_directory)
database_location = "CIS4044-N-SDI-OPENMETEO-PARTIAL.db"

if __name__ == "__main__":
    with sqlite3.connect(database_location) as conn:
        conn.row_factory = sqlite3.Row

        print("1.------------Bar Chart to show the seven day precipitation for a specific city-----------------------------------------------")
        plot_seven_day_precipitation_bar_chart(conn, 2, "2022-05-16")

        print("2.------------Bar Chart to show the specified period for a set of Cities-----------------------------------------------")
        plot_specific_period_bar_chart(conn)

        print("3.------------Bar Chart to show the average yearly precipitation by country-----------------------------------------------")
        plot_average_yearly_precipitation_bar_chart(conn, "2020")

        print("4.------------Grouped Bar Charts to show the min/max/mean temperature and precipitation values for selected city-----------------------------------------------")
        plot_grouped_temperature_and_precipitation_bar_chart(conn, "2021")