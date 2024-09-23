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
# MAGIC DROP TABLE IF EXISTS CLEO.alt_cat_a;
# MAGIC DROP TABLE IF EXISTS CLEO.alt_cat_b;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.at_exclusions;
# MAGIC DROP TABLE IF EXISTS CLEO.at_inclusions;
# MAGIC DROP TABLE IF EXISTS CLEO.eh_exclusions;
# MAGIC DROP TABLE IF EXISTS CLEO.eh_inclusions;
# MAGIC DROP TABLE IF EXISTS CLEO.bh_exclusions;
# MAGIC DROP TABLE IF EXISTS CLEO.bh_inclusions;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.global_exclusions;
# MAGIC DROP TABLE IF EXISTS CLEO.brand_exclusions;
# MAGIC DROP TABLE IF EXISTS CLEO.dept_exclusions;
# MAGIC 
# MAGIC DROP TABLE IF EXISTS CLEO.global_parameters;
# MAGIC 
# MAGIC 
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
