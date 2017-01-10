#!/usr/bin/python

import pandas as pd
from bokeh.charts import Bar, output_file, show
import logging

"""
Reads data set of RISKFACTORSANDACCESSTOCARE.csv
"""

def readcsv(filename,delimiter=','):
    try:
        logging.info("Reading file " )
        return pd.read_csv(filename,sep=delimiter)
    except Exception:
        raise("read dataframe failed....")



dataframe = readcsv("D:\\db_data\chsi_dataset\RISKFACTORSANDACCESSTOCARE.csv")
#gropudata = dataframe.groupby(['CHSI_State_Name'])[['Uninsured']].sum()
p = Bar(dataframe, label='CHSI_State_Name', values='Uninsured,Elderly_Medicare', agg='sum',
        title="Uninsured count by State")
output_file("Bar.html")
show(p)