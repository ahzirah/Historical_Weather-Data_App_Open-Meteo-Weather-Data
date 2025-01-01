# Author: ................ Hyeladzira James Balami.........
# Student ID: .......... D3914083..................

# WEATHER APP (OPEN METEO WEATHER DATA)

## TABLE OF CONTENTS
- Introduction 
- Project Structure
- Features
- System Requirements
- Project Requirements
- Setup and Installation Guide
- Weather App Usage Instructions

## INTRODUCTION
The weather app uses an open meteo API to analyze, visualize and retrieve historical weather data.<br>
The app is designed and developed as a user friendly solution using python, sqlite and matplot libraries, this project demonstrates the application of core programming principles and in real world weather data analysis. 

## PROJECT STRUCTURE
The project follows a modular structure for maintainability and scalability:

- weather_app.py: Main entry point for the application, with menus for each phase.
- phase_1.py: Contains SQLite query functions for data analysis.
- phase_2.py: Includes data visualization functions using Matplotlib.
- phase_3.py: Handles API communication and data storage in SQLite.
- tkinter_gui.py
- CIS4044-N-SDI-OPENMETEO-PARTIAL.db: SQLite database file containing weather and geographical data.

## FEATURES
This weather application, is developed in multiple phases which are: <br>
1. Phase one: This phase includes the quering and processing of data stored in the sqlite3 database with a partially populated database that has been providded. <br>
This phase does only one thing, which is to query data from the sqlite3 database. an example code below to select all countries from the database. <br>
 ``` query = "SELECT * from [countries]" ``` 
2. Phase two: This phases includes the ussage of matplotlib to generate charts based on data taken from the sqlite3 database provided.
in this application, the following charts were used to visualize the trends in the historical weather data:

- Grouped Bar Chart
![alt text](</images_charts/Screenshot 2025-01-01 at 02.05.58.png>)

- Line Chart
![alt text](</images_charts/Screenshot 2025-01-01 at 02.11.34.png>)

- Bar Charts
![alt text](</images_charts/Screenshot 2025-01-01 at 02.14.49.png>)

- Multiline chart
![alt text](</images_charts/Screenshot 2025-01-01 at 02.13.14.png>)

- Scatter Plot
![alt text](</images_charts/Screenshot 2025-01-01 at 02.16.58.png>)

3. Phase three: This phase includes retrieving data from a public web API (open-meteo weather data), updating the data and storing it in the sqlite3 database.

4. Phase four: This is an optional phase which involves further enhancing the application from personal research or the enhancement list provided. in this case, the app was further enhanced by developing a simple graphical user interface using Tkinter, Although the app usage does not entirely depend on this phase alone.

## SYSTEM REQUIREMENTS
- Operating system: windows/linux/MacOS
- Python version: 3.8 or higher

## PROJECT REQUIREMENTS
The following technologies are essential requirements used to run the app without any technical issues
- Programming language - python3
- Requests - for API interaction
- Sqlite3 - for database management
- Matplotlib - for charts visualization
Although sqlite3 is already a part of python's standard library, it does not need to be installed seperately in some cases.<br>
To install all dependencies used in this project, run the following command: <br>
```pip install -r requirements.txt ```  for windiws systems <br>
```pip3 install -r requirements.txt ``` for mac

## SETUP AND INSTALLATION GUIDE
1. step1: Clone the repository
2. step2: Install the dependencies in the requirements.txt file

## WEATHER APP USAGE INSTRUCTIONS
To run the this application, execute the main script below: <br>
``` python3 weather_app.py ``` for command line interface or <br>
``` python3 tkinter_gui.py ``` for Graphic user interface.
Follow the prompts to navigate through phases 1,2 and 3. If the GUI is implemented use the tkinter interface for point and click interaction.
