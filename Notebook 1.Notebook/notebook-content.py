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

# PARAMETERS CELL ********************

rolls_file = "CLEO.wwadbhrolls"
logic_file = "CLEO.wwbhad"

# MARKDOWN ********************

# ## Join Rolls and Logic File based on Product Category


# CELL ********************

import pyspark
from pyspark.sql.functions import concat_ws

dfl = spark.sql("SELECT * FROM CLEO.wwbhad LIMIT 1000")

query = f"SELECT r.*, CASE WHEN b.Revised_Product_Group IS NULL THEN a.Revised_Product_Group \
                 ELSE b.Revised_Product_Group END AS Revised_Product_Group\
                 FROM {rolls_file}  r \
                 LEFT JOIN CLEO.alt_cat_b b ON CONCAT(r.Group,r.Category)=CONCAT(b.Group,b.Category)\
                 LEFT JOIN CLEO.alt_cat_a a ON a.Product_Group=r.Product_Group\
                 LIMIT 1000"
# need to parameterise based on rolls, input and output file (merged)

# Code here to add join col to rolls file based on look up in Alt Cat A and Alt Cat B
df = spark.sql(query)
display(df)
display(dfl)

df2=df.join(dfl, df.Revised_Product_Group == dfl.Product_Group_Logic, "left")
display(df2)
df2.write.mode("overwrite").format("delta").saveAsTable("wwbhad_merged")
