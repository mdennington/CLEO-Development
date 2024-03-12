# Fabric notebook source

# METADATA ********************

# META {
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "894538a7-a495-4a91-a5cb-a71dc284e1a8",
# META       "default_lakehouse_name": "CLEO",
# META       "default_lakehouse_workspace_id": "97377b7f-3479-428a-b07f-e4c97a60fc3b"
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Load Logic Files

# PARAMETERS CELL ********************

file_name = "/lakehouse/default/Files/Test Files/CLEO - Logic Tables.xlsx"
skip_rows = 4
save_table = "ww_sports_logic"
sheet_name = "Sports"

# CELL ********************

import pandas
import pyspark
from pyspark.sql import SparkSession

import os
spark_session = SparkSession.builder.getOrCreate()

df=pandas.read_excel( file_name, sheet_name=sheet_name, skiprows=skip_rows, usecols='B:AA',nrows=24)
df.columns = df.columns.str.replace(' ', '_')
df_sp = spark_session.createDataFrame(df)
df_sp.write.mode("overwrite").format("delta").saveAsTable(save_table)
display(df)

