### Title

* Databricks Spark Python -  Sales Log Data Streaming and Analytics 

### About / Synopsis

* The purpose of this project is to demonstrate a simulation of streaming data in near real-time using Databricks, Apache Spark and Python

### Detailed Description 

* Using Databricks Community Edition, a single-node cluster (DeeptoCluster) is spun up with 15.3 GB Memory and 2 Cores and the latest stable version of Databricks (v8.3.49)
![image](https://user-images.githubusercontent.com/46364751/125229923-c22ad400-e2a5-11eb-8301-adaa25fd8d0b.png)

* The sales_log.zip containing over 80 csv files is uploaded to the "dbfs:/FileStore" directory location
![image](https://user-images.githubusercontent.com/46364751/125230178-5137ec00-e2a6-11eb-84cf-c508e593ffa4.png)

* The file is moved to the local filestore "/tmp/" from the distributed Filestore location and is validated to ensure the file has moved correctly
![image](https://user-images.githubusercontent.com/46364751/125230096-26e62e80-e2a6-11eb-8d17-f424a8e569fc.png)

* The file is then unzipped with all the sales log .csv data files for a fictitious company (Moitra Co.)
![image](https://user-images.githubusercontent.com/46364751/125230378-a8d65780-e2a6-11eb-8b88-50ee37274754.png)

* The "file:/databricks/driver/sales_log/" directory location is checked to see all the unzipped .csv files
![image](https://user-images.githubusercontent.com/46364751/125230481-d7ecc900-e2a6-11eb-8f65-94e64b3dfc08.png)

* Using PySpark, a static df is initially created based on defined schema to test the data ingestion process. The data can be displayed as both table and bar chart
![image](https://user-images.githubusercontent.com/46364751/125230616-25693600-e2a7-11eb-810e-5c667965462f.png)

* Using PySpark's readStream function, each file is read into the readStreamInputDF dataframe. The isStreaming boolean function is also triggered as validation of whether streaming is occurring.
![image](https://user-images.githubusercontent.com/46364751/125230787-842eaf80-e2a7-11eb-839e-4818ad326401.png)

* The data is then written to memory within a high speed pipeline using PySpark's writeStream function and is queried in near real-time to see the change in data quantity being ingested continuously
![image](https://user-images.githubusercontent.com/46364751/125231279-77f72200-e2a8-11eb-8a60-9f15d9fa53d2.png)

![image](https://user-images.githubusercontent.com/46364751/125231294-7ded0300-e2a8-11eb-97ca-9634d7695b13.png)

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
* Dataset: https://github.com/bsullins/bensullins.com-freebies
* Lesson: Apache Spark Essential Training - Ben Sullins: https://www.linkedin.com/learning/apache-spark-essential-training/

### Support

* This project is a standalone development initiative without any ongoing support

