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

# #### Filter Rolls file based on Exclusions Files
# There are four exclusion files
# - Global
# - Brand
# - Deparment
# - FC (different for each FC)
# 


# PARAMETERS CELL ********************

rollsFile = "wwadbhrolls"
exclusionFile = "bh_exclusions"
outputTable = "wwadbh_filtered"

# CELL ********************

query = f"SELECT * FROM CLEO.{rollsFile} r \
                WHERE r.brand not in (select bex.brand FROM CLEO.brand_exclusions bex) AND\
                      r.productId not in(select gex.SKU FROM CLEO.global_exclusions gex) AND\
                      r.Buying_Group not in (select dex.DEPARTMENT FROM CLEO.dept_exclusions dex) AND\
                      r.productId not in (select fcex.Option FROM CLEO.{exclusionFile} fcex)"


df = spark.sql(query)

tableName = f"{outputTable}"

df.write.mode("overwrite").format("delta").saveAsTable(tableName)

display(df)

# CELL ********************

df = spark.sql("SELECT * FROM CLEO.wwadbhrolls r WHERE r.Brand = 'Boohoo' LIMIT 1000")
display(df)
