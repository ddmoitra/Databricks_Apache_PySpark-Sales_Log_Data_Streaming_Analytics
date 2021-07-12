### Title

* Databricks Spark Python -  Sales Log Data Streaming and Analytics 

### About / Synopsis

* The purpose of this project is to demonstrate a simulation of streaming data in near real-time using Databricks, Apache Spark and Python

### Detailed Description 

* Using Databricks Community Edition, a single-node cluster (DeeptoCluster) is spun up with 15.3 GB Memory and 2 Cores and the latest stable version of Databricks (v8.3.49)

* The sales_log.zip containing over 80 csv files is uploaded to the "dbfs:/FileStore" directory location

* The file is moved to the local filestore "/tmp/" from the distributed Filestore location and is validated to ensure the file has moved correctly

* The file is then unzipped with all the sales log .csv data files for a fictitious company (Moitra Co.)

* The "file:/databricks/driver/sales_log/" directory location is checked to see all the unzipped .csv files

* Using PySpark, a static df is initially created based on defined schema to test the data ingestion process. The data can be displayed as both table and bar chart

* Using PySpark's readStream function, each file is read into the readStreamInputDF dataframe. The isStreaming boolean function is also triggered as validation of whether streaming is occurring.


* The data is then written to memory within a high speed pipeline using PySpark's writeStream function and is queried in near real-time to see the change in data quantity being ingested continuously


### Installation / Software Requirements

* The following tools were used in this project:

 * Python 3
 * Apache Spark 3.1.1
 * Databricks 8.3.49 - July 2021

### Usage

* Create an account on the Community edition of Databricks - https://community.cloud.databricks.com

* Use/upload any of the three filetypes loaded into GitHub for your review:
	* Moitra Co._Sales_Log_Streaming_Data.dbc
	* Moitra Co._Sales_Log_Streaming_Data.ipynb
	* Moitra Co._Sales_Log_Streaming_Data.py

* The sales log source data is also provided as well as a zip file - upload and unzip in Databricks

* Update file paths as needed and run the script cells

### License / Citation

* Python GPU License: https://docs.python.org/3.7/license.html
* Apache License: https://www.apache.org/licenses/LICENSE-2.0
* Databricks License - https://databricks.com/ce-termsofuse
* Dataset: https://www.kaggle.com/joniarroba/noshowappointments

### Support

* This project is a standalone development initiative without any ongoing support

