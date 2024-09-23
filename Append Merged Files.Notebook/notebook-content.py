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

# ## Append Files together


# CELL ********************

df = spark.sql("SELECT * FROM CLEO.wwadat_merged\
                UNION ALL\
                SELECT * FROM CLEO.wwadbh_merged\
                UNION ALL\
                SELECT * FROM CLEO.wwadeh_merged\
                UNION ALL\
                SELECT * FROM CLEO.wwpbat_merged\
                UNION ALL\
                SELECT * FROM CLEO.wwpbbh_merged\
                UNION ALL\
                SELECT * FROM CLEO.wwpbeh_merged\
                UNION ALL\
                SELECT * FROM CLEO.wwsportsat_merged\
                UNION ALL\
                SELECT * FROM CLEO.wwsportsbh_merged\
                UNION ALL\
                SELECT * FROM CLEO.wwsportseh_merged\
                UNION ALL\
                SELECT * FROM CLEO.wwventureat_merged\
                UNION ALL\
                SELECT * FROM CLEO.wwventurebh_merged\
                UNION ALL\
                SELECT * FROM CLEO.wwventureeh_merged\
                UNION ALL\
                SELECT * FROM CLEO.mwadat_merged\
                UNION ALL\
                SELECT * FROM CLEO.mwadbh_merged\
                UNION ALL\
                SELECT * FROM CLEO.mwadeh_merged\
                UNION ALL\
                SELECT * FROM CLEO.mwpbat_merged\
                UNION ALL\
                SELECT * FROM CLEO.mwpbbh_merged\
                UNION ALL\
                SELECT * FROM CLEO.mwpbeh_merged\
                UNION ALL\
                SELECT * FROM CLEO.mwsportsat_merged\
                UNION ALL\
                SELECT * FROM CLEO.mwsportsbh_merged\
                UNION ALL\
                SELECT * FROM CLEO.mwsportseh_merged\
                UNION ALL\
                SELECT * FROM CLEO.mwventureat_merged\
                UNION ALL\
                SELECT * FROM CLEO.mwventurebh_merged\
                UNION ALL\
                SELECT * FROM CLEO.mwventureeh_merged")
display(df.count())

df.write.mode("overwrite").format("delta").saveAsTable("cleo_merged")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
