# Databricks notebook source
# MAGIC %fs ls 'dbfs:/FileStore/'

# COMMAND ----------

dbutils.fs.cp("/FileStore/sales_log.zip", "file:/tmp/sales_log.zip")

# COMMAND ----------

dbutils.fs.mv("dbfs:/FileStore/sales_log.zip","/tmp/sales_log.zip")

# COMMAND ----------

# MAGIC %fs ls "/tmp/"

# COMMAND ----------

# MAGIC %sh ls /tmp/

# COMMAND ----------

# MAGIC %sh unzip /tmp/sales_log.zip

# COMMAND ----------

# MAGIC %fs ls 'file:/databricks/driver/sales_log/'

# COMMAND ----------

from pyspark.sql.types import *

path = "file:/databricks/driver/sales_log/"

salesSchema = StructType([
  StructField("OrderId", DoubleType(), True),
  StructField("OrderDate", StringType(), True),
  StructField("Quantity", DoubleType(), True),
  StructField("DiscountPct", DoubleType(), True),
  StructField("Rate", DoubleType(), True),
  StructField("SaleAmount", DoubleType(), True),
  StructField("CustomerName", StringType(), True),
  StructField("State", StringType(), True),
  StructField("Region", StringType(), True),
  StructField("ProductKey", StringType(), True),
  StructField("RowCount", DoubleType(), True),
  StructField("ProfitMargin", DoubleType(), True)
])

df = (spark.read.schema(salesSchema).csv(path))

display(df)

# COMMAND ----------

from pyspark.sql.functions import *

#Reads in files as a stream one file at a time
readStreamInputDF = (spark.readStream.schema(salesSchema).option('maxFilesPerTrigger',1).csv(path))

streamingCountsDF = (readStreamInputDF.select("ProductKey","SaleAmount").groupBy("ProductKey").sum())

streamingCountsDF.isStreaming

# COMMAND ----------

queryStream = (streamingCountsDF.writeStream.format("memory").queryName("sales_stream").outputMode("complete").start())

# COMMAND ----------

# MAGIC %sql select * from sales_stream order by 2 desc limit 100
