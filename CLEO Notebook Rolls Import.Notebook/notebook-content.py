# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "894538a7-a495-4a91-a5cb-a71dc284e1a8",
# META       "default_lakehouse_name": "CLEO",
# META       "default_lakehouse_workspace_id": "97377b7f-3479-428a-b07f-e4c97a60fc3b"
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Load Rolls Files

# PARAMETERS CELL ********************

file_name = "Test Files/CLEO - Amendments.xlsx"
save_table = "at_inclusions"
sheet_name = "AT Inclusions"


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************


# CELL ********************

# Import Files from Excel and write to lakehouse
import pandas
import pyspark
from pyspark.sql import SparkSession

import os
spark_session = SparkSession.builder.getOrCreate()
full_file_name = "/lakehouse/default/Files/" + file_name
df=pandas.read_excel( full_file_name, sheet_name=sheet_name, header=0)
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('(', '')
df.columns = df.columns.str.replace(')', '')
df_sp = spark_session.createDataFrame(df)
df_sp.write.option("overwriteSchema", "true").mode("overwrite").format("delta").saveAsTable(save_table)
display(df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
