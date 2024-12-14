

#----------------------------------------------------#
#........ Author: HYELADZIRA JAMES BALAMI...........
#.........Student_ID: D3914083......................
#----------------------------------------------------#





# PHASE 2 - BASIC GRAPHS USING MATPLOTLIB


# Imports
import matplotlib as plt
import phase_1 as module_code
import sqlite3


def plot():
   with sqlite3 .connect("../ICA_database/CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as conn:
      try:
      
        data = module_code.select_all_countries2(conn)
        # -TODO add plot code to use the data

      except Exception as e:
        pass
   
      
      