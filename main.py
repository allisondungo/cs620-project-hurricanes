# CS 620
# Semester Data Project: Hurricane Tracking
# @author: Allison Dungo

from pandas import DataFrame
import pandas as pd
import numpy as np

if __name__ == '__main__':
    may_outlook = pd.read_csv("may_hurricane_outlook.csv")
    hurricanes = pd.read_csv("hurricane_data_after.csv")
    summaries = pd.read_csv("hurricane_summaries.csv")

    years = may_outlook.year.unique() # put individual years into an array

    for x in years:
        expected_storms = may_outlook['# of expected named storms'][may_outlook['year'] == x]
        print("Year: ", x)
        print("# of Expected Named Storms: ", expected_storms.values)
        print("# of Actual Storms: ", len(summaries[summaries['year'] == x]), "\n")