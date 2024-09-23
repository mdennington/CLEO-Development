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

# #### Filter Rolls file based on Exclusions Files
# There are four exclusion files
# - Global
# - Brand
# - Deparment
# - FC (different for each FC)
# 


# PARAMETERS CELL ********************

rollsFile = "wwpbehrolls"
exclusionFile = "eh_exclusions"
outputTable = "wwpbeh_filtered"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import lit


query = f"SELECT * FROM CLEO.{rollsFile} r \
                WHERE r.brand not in (select bex.brand FROM CLEO.brand_exclusions bex) AND\
                      r.productId not in(select gex.SKU FROM CLEO.global_exclusions gex) AND\
                      r.Buying_Group not in (select dex.DEPARTMENT FROM CLEO.dept_exclusions dex) AND\
                      r.productId not in (select fcex.Option FROM CLEO.{exclusionFile} fcex)"


df = spark.sql(query)

tableName = f"{outputTable}"
newdf = df.withColumn("Gender", lit(rollsFile[:2]))
newdf.write.mode("overwrite").format("delta").saveAsTable(tableName)

display(newdf)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
