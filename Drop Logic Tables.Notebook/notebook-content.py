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

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.wwbhad;
# MAGIC DROP TABLE IF EXISTS CLEO.wwehad;
# MAGIC DROP TABLE IF EXISTS CLEO.wwatad;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.wwbhpb;
# MAGIC DROP TABLE IF EXISTS CLEO.wwehpb;
# MAGIC DROP TABLE IF EXISTS CLEO.wwatpb;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.wwbhsports;
# MAGIC DROP TABLE IF EXISTS CLEO.wwehsports;
# MAGIC DROP TABLE IF EXISTS CLEO.wwatsports;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.wwbhventure;
# MAGIC DROP TABLE IF EXISTS CLEO.wwehventure;
# MAGIC DROP TABLE IF EXISTS CLEO.wwatventure;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.mwbhad;
# MAGIC DROP TABLE IF EXISTS CLEO.mwehad;
# MAGIC DROP TABLE IF EXISTS CLEO.mwatad;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.mwbhpb;
# MAGIC DROP TABLE IF EXISTS CLEO.mwehpb;
# MAGIC DROP TABLE IF EXISTS CLEO.mwatpb;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.mwbhsports;
# MAGIC DROP TABLE IF EXISTS CLEO.mwehsports;
# MAGIC DROP TABLE IF EXISTS CLEO.mwatsports;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.mwehventure;
# MAGIC DROP TABLE IF EXISTS CLEO.mwbhventure;
# MAGIC DROP TABLE IF EXISTS CLEO.mwatventure;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
