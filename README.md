# spark-get-file-name
Spark job to get orc format file name for column filter in the data.

The file runs on pyspark module and by default reads data from the hdfs file path mentioned in the file.
It runs on spark version Spark-2.2 or above.

Below is the command to submit the spark job:
spark2-submit --master yarn --deploy-mode client --executor-memory=4g --num-executors=3 --executor-cores=2 --driver-memory=2g find_filename.py
