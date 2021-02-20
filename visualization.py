#!interpreter python.exe visualization.py
# -*- coding: utf-8 -*-

"""
Description: Main file - visualizing all the sorting algorithms
             set in the algorithms directory
License:
"""

# => WINDOW CLASS FILE
import window

# => DATA FILE
import data

__author__ = "Adriskk"
__copyright__ = "Copyright 2020, Sorting Algorithms Visualization project"
__credits__ = ["Adriskk"]
__license__ = ""
__version__ = "1.0.0"
__email__ = "adrian_iskra@o2.pl"

if __name__ == "__main__":
    for i in range(len(data.algorithms)):
        screen = window.Window(data.algorithms[i])
        screen.loop()

