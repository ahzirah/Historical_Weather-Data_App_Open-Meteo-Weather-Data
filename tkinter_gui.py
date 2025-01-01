import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os
import phase_1 as queries
from phase_2 import plot_open_meteo_weather_data_app
from phase_3 import data_retrieval_and_storage

# Set the working directory
file_path = os.path.abspath(__file__)
working_directory = os.path.dirname(file_path)
os.chdir(working_directory)

# Database location
database_location = "CIS4044-N-SDI-OPENMETEO-PARTIAL.db"


class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry("800x600")

        # Main Menu
        self.create_main_menu()

    def create_main_menu(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Weather App Main Menu", font=("Arial", 18)).pack(pady=20)
        tk.Button(self, text="Phase 1: SQLite Queries", command=self.phase_1_menu, width=40).pack(pady=10)
        tk.Button(self, text="Phase 2: Graph Plots", command=self.phase_2_menu, width=40).pack(pady=10)
        tk.Button(self, text="Phase 3: Data Retrieval", command=self.phase_3_menu, width=40).pack(pady=10)
        tk.Button(self, text="Exit", command=self.destroy, width=40, fg="red").pack(pady=20)

    def phase_1_menu(self):
        def execute_query(query_func, *args):
            try:
                with sqlite3.connect(database_location) as conn:
                    conn.row_factory = sqlite3.Row
                    result = query_func(conn, *args)
                    messagebox.showinfo("Query Result", f"Data: {result}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Phase 1: SQLite Queries", font=("Arial", 18)).pack(pady=20)

        options = [
            ("Select All Countries", lambda: execute_query(queries.select_all_countries)),
            ("Select All Cities", lambda: execute_query(queries.select_all_cities)),
            ("Average Annual Temperature", lambda: execute_query(queries.average_annual_temperature, 1, "2022")),
            ("Average Seven Day Precipitation", lambda: execute_query(queries.average_seven_day_precipitation, 1, "2022-06-03")),
            ("Average Mean Temperature by City", lambda: execute_query(queries.average_mean_temp_by_city, "2022-05-19", "2022-05-30")),
            ("Average Annual Precipitation by Country", lambda: execute_query(queries.average_annual_precipitation_by_country, "2022")),
            ("Min, Max and Mean Temperature and Precipitation By City", lambda: execute_query(queries.min_max_mean_temperature_and_precipitation_by_city, "2022")),
            ("Minimum and Maximum Monthly Temperature by City", lambda: execute_query(queries.minimum_and_maximum_monthly_temperature_by_city, 1, "2022")),
            ("Average Temperature VS Average Precipitation", lambda: execute_query(queries.average_temperature_vs_average_precipitation, 1, "2022-06-03")),
            ("Seven Day Temperature by City", lambda: execute_query(queries.seven_day_temperature_by_city, 1, "2022-06-03")),
            ("Seven Day Precipitation", lambda: execute_query(queries.seven_day_precipitation, 1, "2022-06-03")),

        ]

        for label, command in options:
            tk.Button(self, text=label, command=command, width=50).pack(pady=5)

        tk.Button(self, text="Back to Main Menu", command=self.create_main_menu, width=30).pack(pady=20)

    def phase_2_menu(self):
        def visualize_city_data(country_id, city_id):
            try:
                with sqlite3.connect(database_location) as conn:
                    conn.row_factory = sqlite3.Row
                    plot_open_meteo_weather_data_app(conn, city_id)
                    messagebox.showinfo("Success", f"Visualization for City ID {city_id} completed.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Phase 2: Graph Plots", font=("Arial", 18)).pack(pady=20)

        countries = {"1": "GREAT BRITAIN", "2": "FRANCE"}
        cities_in_countries = {
            "1": {"1": "MIDDLESBROUGH", "2": "LONDON"},
            "2": {"3": "PARIS", "4": "TOULOUSE"}
        }

        tk.Label(self, text="Select a Country", font=("Arial", 14)).pack(pady=10)
        country_var = tk.StringVar(value="1")
        for country_id, country_name in countries.items():
            ttk.Radiobutton(self, text=country_name, variable=country_var, value=country_id).pack(anchor="w")

        tk.Label(self, text="Select a City", font=("Arial", 14)).pack(pady=10)
        city_var = tk.StringVar(value="1")

        def update_city_options():
            for widget in city_frame.winfo_children():
                widget.destroy()

            selected_country = country_var.get()
            for city_id, city_name in cities_in_countries[selected_country].items():
                ttk.Radiobutton(city_frame, text=city_name, variable=city_var, value=city_id).pack(anchor="w")

        city_frame = tk.Frame(self)
        city_frame.pack(pady=10)
        update_city_options()

        country_var.trace("w", lambda *args: update_city_options())

        tk.Button(self, text="Visualize", command=lambda: visualize_city_data(country_var.get(), city_var.get()), width=30).pack(pady=20)
        tk.Button(self, text="Back to Main Menu", command=self.create_main_menu, width=30).pack(pady=20)

    def phase_3_menu(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Phase 3: Data Retrieval", font=("Arial", 18)).pack(pady=20)

        tk.Button(self, text="Retrieve and Store Weather Data", command=self.retrieve_weather_data, width=50).pack(pady=10)
        tk.Button(self, text="View Stored Weather Data", command=self.view_stored_data, width=50).pack(pady=10)
        tk.Button(self, text="Back to Main Menu", command=self.create_main_menu, width=30).pack(pady=20)

    def retrieve_weather_data(self):
        try:
            data_retrieval_and_storage()
            messagebox.showinfo("Success", "Weather data retrieved and stored successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def view_stored_data(self):
        try:
            with sqlite3.connect(database_location) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.execute("SELECT * FROM weather_data")
                data = cursor.fetchall()
                if data:
                    result = "\n".join([str(dict(row)) for row in data])
                    messagebox.showinfo("Stored Data", result)
                else:
                    messagebox.showinfo("Stored Data", "No data found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
