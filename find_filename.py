from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

def filename(path):
    return path

sourceFile = udf(filename, StringType())
spark = SparkSession.builder.appName("Find FileName").getOrCreate()
A = spark.read.orc('output/ss7_model/map')
A.filter(A['cosName']=='#Default COS#').select(sourceFile(input_file_name())).show(20,False)