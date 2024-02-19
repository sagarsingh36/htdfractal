# Databricks notebook source
spark.conf.set(
    "fs.azure.account.key.databrickstorage966.dfs.core.windows.net","IZ9oeJFp8vOmIj6aDWzunh5+gC02uSq/3506HTvjF/DxOVYZRCg2QEaoG6LWK1Y4Mcunbskx6RAS+AStvgvYQQ==")

# COMMAND ----------

display(dbutils.fs.ls("abfss://containerdata@databrickstorage966.dfs.core.windows.net"))

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.<storage-account>.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.<storage-account>.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.<storage-account>.dfs.core.windows.net", dbutils.secrets.get(scope="<scope>", key="<sas-token-key>"))

# COMMAND ----------


