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

# ## Append Files together


# CELL ********************

df = spark.sql("SELECT COUNT(*) FROM CLEO.wwadbh_merged")
display(df)

# CELL ********************

df = spark.sql("SELECT COUNT(*) FROM CLEO.wwadeh_merged")
display(df)

# CELL ********************

df = spark.sql("SELECT * FROM CLEO.wwadat_merged")
display(df)

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
                SELECT * FROM CLEO.wwventureeh_merged")
display(df.count())

df.write.mode("overwrite").format("delta").saveAsTable("cleo_merged")
