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
# MAGIC DROP TABLE if exists cleo.mwadatrolls;
# MAGIC DROP TABLE if exists cleo.mwadbhrolls;
# MAGIC DROP TABLE if exists cleo.mwadehrolls;
# MAGIC 
# MAGIC DROP TABLE if exists cleo.mwpbatrolls;
# MAGIC DROP TABLE if exists cleo.mwpbbhrolls;
# MAGIC DROP TABLE if exists cleo.mwpbehrolls;
# MAGIC 
# MAGIC DROP TABLE if exists cleo.mwventureatrolls;
# MAGIC DROP TABLE if exists cleo.mwventurebhrolls;
# MAGIC DROP TABLE if exists cleo.mwventureehrolls;
# MAGIC 
# MAGIC DROP TABLE if exists cleo.mwsportsatrolls;
# MAGIC DROP TABLE if exists cleo.mwsportsbhrolls;
# MAGIC DROP TABLE if exists cleo.mwsportsehrolls;
# MAGIC 
# MAGIC DROP TABLE if exists cleo.wwadatrolls;
# MAGIC DROP TABLE if exists cleo.wwadbhrolls;
# MAGIC DROP TABLE if exists cleo.wwadehrolls;
# MAGIC 
# MAGIC DROP TABLE if exists cleo.wwpbatrolls;
# MAGIC DROP TABLE if exists cleo.wwpbbhrolls;
# MAGIC DROP TABLE if exists cleo.wwpbehrolls;
# MAGIC 
# MAGIC DROP TABLE if exists cleo.wwventureatrolls;
# MAGIC DROP TABLE if exists cleo.wwventurebhrolls;
# MAGIC DROP TABLE if exists cleo.wwventureehrolls;
# MAGIC 
# MAGIC DROP TABLE if exists cleo.wwsportsatrolls;
# MAGIC DROP TABLE if exists cleo.wwsportsbhrolls;
# MAGIC DROP TABLE if exists cleo.wwsportsehrolls;
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
