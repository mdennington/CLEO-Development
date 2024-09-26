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

# PARAMETERS CELL ********************

rolls_file = "CLEO.mwventureat_filtered"
logic_file = "CLEO.mwatventure"
output_table = "mwatventure_merged"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Join Rolls and Logic File based on Product Category


# CELL ********************

import pyspark
from pyspark.sql.functions import concat_ws

query1 = f"SELECT * FROM {logic_file}"

dfl = spark.sql(query1)

query = f"SELECT r.*, CASE WHEN b.Revised_Product_Group IS NULL THEN a.Revised_Product_Group \
                 ELSE b.Revised_Product_Group END AS Revised_Product_Group\
                 FROM {rolls_file}  r \
                 LEFT JOIN CLEO.alt_cat_b b ON CONCAT(r.Group,r.Category)=CONCAT(b.Group,b.Category)\
                 LEFT JOIN CLEO.alt_cat_a a ON a.Product_Group=r.Product_Group\
                 LIMIT 1000"

# Join Logic and Rolls File based on RPG
df = spark.sql(query)
df2=df.join(dfl, df.Revised_Product_Group == dfl.Product_Group_Logic, "left")
display(df2)
df2.write.mode("overwrite").format("delta").saveAsTable(f"{output_table}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
