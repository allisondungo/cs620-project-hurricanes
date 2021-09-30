# CS 620
# Semester Data Project: Hurricane Tracking
# @author: Allison Dungo

from pandas import DataFrame
import pandas as pd
import numpy as np

if __name__ == '__main__':
    may_outlook = pd.read_csv("may_hurricane_outlook.csv")
    hurricanes = pd.read_csv("hurricane_data_after.csv")
    print(hurricanes.date)