# Databricks notebook source
spark.conf.set("fs.azure.account.auth.type.databrickstorage966.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.databrickstorage966.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.databrickstorage966.dfs.core.windows.net", "?sv=2022-11-02&ss=bfqt&srt=c&sp=rwdlacupyx&se=2024-02-19T15:10:58Z&st=2024-02-19T07:10:58Z&spr=https&sig=yWRKty%2B3Ghq7ijAgbwTMDYFkhbOO3B8cCX0bFNILO4E%3D")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@databrickstorage966.dfs.core.windows.net"))

# COMMAND ----------


