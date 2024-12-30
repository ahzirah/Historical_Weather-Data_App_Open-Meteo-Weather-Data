

###########################----------------------------------------------------##############################
###########################........ Author: HYELADZIRA JAMES BALAMI............##############################
###########################.........Student_ID: D3914083.......................##############################
###########################----------------------------------------------------##############################


#................................. WEATHER APP - USER INTERFACE AND APP USABILITY............................#



# IMPORTS
import sqlite3
import os
import phase_1 as queries
from phase_2 import plot_open_meteo_weather_data_app
from phase_3 import data_retrieval_and_storage


file_path = os.path.abspath(__file__)
working_directory = os.path.dirname(file_path)
os.chdir(working_directory)
database_location = "CIS4044-N-SDI-OPENMETEO-PARTIAL.db"
with sqlite3.connect(database_location) as conn:
    conn.row_factory = sqlite3.Row


# ..............PHASE 1 MENU.............................
def phase_1_menu():
        
        print("\n--- PHASE 1 - PYTHON AND SQLITE3 DATABASE QUERIES ---")
        print("--------------------------------------------------------")
        print("\n")
        print("1. Select All Countries")
        print("2. Select All Cities")
        print("3. Average Annual Temperature")
        print("4. Average Seven Day Precipitation")
        print("5. Average Mean Temperature By City")
        print("6. Average Annual Precipitation By Country-")
        print("7. Min, Max and Mean Temperature and Precipitation By City")
        print("8. Minimum and Maximum Monthly Temperature By City")
        print("9. Average Temperature By City And Country")
        print("10. Seven Day Temperature By City And Country")
        print("11. Seven Day Precipitation By City")
        print("0. Exit to Main Menu")

        choice = input("Select an option from the menu to view: ")
        if choice == "1":
                data = queries.select_all_countries(conn)
                print("Data:", data)
        elif choice == "2":
                data = queries.select_all_cities(conn)
                print("Data:", data)
        elif choice == "3":
                city_id = int(input("Enter City ID: "))
                data = queries.average_annual_temperature(conn, city_id, "2022")
                print("Data:", data)
        elif choice == "4":
                city_id = int(input("Enter City ID: "))
                data = queries.average_seven_day_precipitation(conn, city_id, "2022-06-03")
                print("Data:", data)
        elif choice == "5":
                city_id = int(input("Enter City ID: "))
                data = queries.average_mean_temp_by_city(conn, "2022-05-19", "2022-05-30")
                print("Data:", data)
        elif choice == "6":
                data = queries.average_annual_precipitation_by_country(conn, "2022")
                print("Data:", data)
        elif choice == "7":
                city_id = int(input("Enter City ID: "))
                data = queries.min_max_mean_temperature_and_precipitation_by_city(conn, "2022")
                print("Data:", data)
        elif choice == "8":
                city_id = int(input("Enter City ID: "))
                data = queries.minimum_and_maximum_monthly_temperature_by_city(conn, city_id, "2022")
                print("Data:", data)
        elif choice == "9":
                city_id = int(input("Enter City ID: "))
                data = queries.average_temperature_vs_average_precipitation(conn, city_id, "2022-06-03")
                print("Data:", data)
        elif choice == "10":
                city_id = int(input("Enter City ID: "))
                data = queries.seven_day_temperature_by_city(conn, city_id, "2022-06-03")
                print("Data:", data)
        elif choice == "11":
                city_id = int(input("Enter City ID: "))
                data = queries.seven_day_precipitation(conn, city_id, "2022-06-03")
                print("Data:", data)
        elif choice == "0":
                print("Exiting to main menu")
        else:
                print("Invalid choice! Please try again.")



    # ..............PHASE 2 MENU.............................
def phase_2_menu():
        print("\n--- PHASE 2 - BASIC GRAPH PLOTS USING MATPLOTLIB LIBRARY ---")
        print("--------------------------------------------------------")
        print("\n")

        countries = {"1": "GREAT BRITAIN", "2": "FRANCE"}
        cities = {"1": "MIDDLESBROUGH", "2": "LONDON", "3": "PARIS", "4": "TOULOUSE"}

        with sqlite3.connect(database_location) as conn:
          conn.row_factory = sqlite3.Row
        while True:
            print("AVAILBLE LOCATIONS:")
            for country_id, country_name in countries.items():
                    print(f"COUNTRY: {country_name} (ID: {country_id})")
            for city_id, city_name in cities.items():
                    print(f"  CITY: {city_name} (ID: {city_id})")

            user_input = input("Enter 'Country ID City ID' for visualization (e.g., '1 2') or 'x' to exit: ").strip()
            if user_input.lower() == 'x':
                    print("Exiting the application.")
                    break
            try:
                    country_id, city_id = map(int, user_input.split())
                    if str(country_id) in countries and str(city_id) in cities:
                        plot_open_meteo_weather_data_app(conn, city_id)
                    else:
                        print("Invalid IDs. Please try again.")
            except ValueError:
                    print("Invalid input format. Use 'Country ID City ID'.")



    # ..............PHASE 2 MENU............................. 
def phase_3_menu():
        while True:
            print("\n--- PHASE 3 - DATA RETRIEVAL AND STORAGE ---")
            print("--------------------------------------------------------")
            print("\n")
            print("1. Fetch and Store Weather Data")
            print("2. View Stored Weather Data")
            print("0. Exit to Main Menu")
            
            choice = input("Enter your choice: ")
            if choice == "1":
                data_retrieval_and_storage()
            # elif choice == "2":
            #     view_stored_weather_data()
            # elif choice == "3":
            #     clear_weather_data()
            elif choice == "0":
                break
            else:
                print("Invalid choice! Please try again.")


# ...........................................MAIN MENU.........................................

if __name__ == "__main__":
    try:
        with sqlite3.connect(database_location) as conn:
            conn.row_factory = sqlite3.Row
            while True:
                print("\n -------------- Weather App Main Menu ----------------")
                print("1. PHASE 1: PYTHON AND SQLITE3 DATABASE QUERIES")
                print("2. PHASE 2: BASIC GRAPH PLOTS USING MATPLOTLIB LIBRARY")
                print("3. PHASE 3: DATA RETRIEVAL AND STORAGE")
                print("0. Exit")

                choice = input("Enter your choice: ")
                if choice == "1":
                    phase_1_menu()
                elif choice == "2":
                    phase_2_menu()
                elif choice == "3":
                    phase_3_menu()
                elif choice == "0":
                    print("Exiting the application. Goodbye!")
                    break
                else:
                    print("Invalid choice! Please try again.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
