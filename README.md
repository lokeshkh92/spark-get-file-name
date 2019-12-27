# spark-get-file-name
Spark job to get orc format file name for column filter in the data.

The file runs on pyspark module and by default reads data from the hdfs file path mentioned in the file.

In the find_filename.py python file one needs to mention the orc file path and the column filter value in pyspark dataframe format, please file below the sample:

orc file path: hdfs://nnha/user/lokesh/output/

column filter to be used in pyspark dataframe format: A['cosName']=='#Default COS#'

Software Dependencies:
1. Spark version Spark-2.2 or above.
2. Python-2.7 or above


##################################################################################

Below is the command to submit the spark job:

spark2-submit --master yarn --deploy-mode client --executor-memory=4g --num-executors=3 --executor-cores=2 --driver-memory=2g find_filename.py
