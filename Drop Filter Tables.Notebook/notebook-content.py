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
# MAGIC DROP TABLE IF EXISTS CLEO.wwadbh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.wwadeh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.wwadat_filtered;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.wwpbbh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.wwpbeh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.wwpbat_filtered;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.wwsportsbh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.wwsportseh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.wwsportsat_filtered;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.wwventurebh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.wwventureeh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.wwventureat_filtered;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.mwadbh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.mwadeh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.mwadat_filtered;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.mwpbbh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.mwpbeh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.mwpbat_filtered;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.mwsportsbh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.mwsportseh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.mwsportsat_filtered;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.mwventurebh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.mwventureeh_filtered;
# MAGIC DROP TABLE IF EXISTS CLEO.mwventureat_filtered;


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
