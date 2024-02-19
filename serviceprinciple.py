# Databricks notebook source
##code for service principle
client_id = "413f4d9e-9578-4840-9e80-85838a7035a7"
tenant_id = "c3d0f98e-c740-4d84-859d-b0b418502757"
client_secret = "eOH8Q~AVYWekn6XND0ytusrc12kTgqaxZG14zc4R"

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.databrickstorage966.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.databrickstorage966.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.databrickstorage966.dfs.core.windows.net", client_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.databrickstorage966.dfs.core.windows.net", client_secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.databrickstorage966.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@databrickstorage966.dfs.core.windows.net/"))

# COMMAND ----------


