from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

def filename(path):
    return path

sourceFile = udf(filename, StringType())
spark = SparkSession.builder.appName("Find FileName").getOrCreate()
A = spark.read.orc('<orc file path>')
A.filter(<column filter to be used>).select(sourceFile(input_file_name())).show(20,False)
