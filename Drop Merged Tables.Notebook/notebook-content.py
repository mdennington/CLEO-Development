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
# MAGIC DROP TABLE IF EXISTS CLEO.wwadbh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.wwadeh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.wwadat_merged;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.wwpbbh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.wwpbeh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.wwpbat_merged;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.wwsportsbh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.wwsportseh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.wwsportsat_merged;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.wwventurebh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.wwventureeh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.wwventureat_merged;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.mwadbh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.mwadeh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.mwadat_merged;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.mwpbbh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.mwpbeh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.mwpbat_merged;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.mwsportsbh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.mwsportseh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.mwsportsat_merged;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.mwventurebh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.mwventureeh_merged;
# MAGIC DROP TABLE IF EXISTS CLEO.mwventureat_merged;


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
