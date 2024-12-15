

#----------------------------------------------------#
#........ Author: HYELADZIRA JAMES BALAMI...........
#.........Student_ID: D3914083......................
#----------------------------------------------------#





# PHASE 2 - BASIC GRAPHS USING MATPLOTLIB


# Imports
import matplotlib as plt
import phase_1 as queries
import sqlite3
import os

file_path = os.path.abspath(__file__)
working_directory = os.path.dirname(file_path)
os.chdir(working_directory)
database_location = "CIS4044-N-SDI-OPENMETEO-PARTIAL.db"


def plot():
   
  with sqlite3.connect(database_location) as conn:
    try:
        
      data = queries.select_all_countries2(conn)
      # -TODO add plot code to use the data

    except Exception as e:
          pass
    
      
      