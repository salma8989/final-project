import pyspark
import os

from dotenv import load_dotenv
from pathlib import Path
from pyspark.sql.types import *

#Initialization
dotenv_path = Path('/resources/.env')
load_dotenv(dotenv_path=dotenv_path)

#Get environment postgres variables
postgres_host = os.getenv('POSTGRES_CONTAINER_NAME')
postgres_db = os.getenv('POSTGRES_DB')
postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')

#Create SparkContext and SparkSession
sparkcontext = pyspark.SparkContext.getOrCreate(conf=(
                pyspark
                .SparkConf()
                .setAppName('finalProject')
                .setMaster('local')
                .set("spark.jars","/jar/postgresql-42.6.0.jar")
                ))
sparkcontext.setLogLevel("WARN")

spark = pyspark.sql.SparkSession(sparkcontext.getOrCreate())
spark

#JDBC to read data from postgres
jdbc_url = f'jdbc:postgresql://{postgres_host}/{postgres_db}'
jdbc_properties = {
                    'user': postgres_user,
                    'password': postgres_password,
                    'driver': 'org.postgresql.Driver'
                    
}

expeditions_df = spark.read.jdbc(
                                  jdbc_url,
                                  'public.expeditions',
                                  properties=jdbc_properties
)
members_df = spark.read.jdbc(
                                  jdbc_url,
                                  'public.members',
                                  properties=jdbc_properties
)
peaks_df = spark.read.jdbc(
                                  jdbc_url,
                                  'public.peaks',
                                  properties=jdbc_properties
)

members_df1 = members_df.select("expedition_id", "peak_id", "member_id", "sex", "age", "citizenship", "success")
peaks_df1 = peaks_df.select("peak_id", "height_metres", "climbing_status")

#Set join preferences between expedition_df to members_df1 and peaks_df1
spark.conf.set("spark.sql.join.preferSortMergeJoin", "false")
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "1000000000")

#Perform broadcast hash join
broadcast_df = members_df1.join(broadcast(expedition_df), "expedition_id").join(broadcast(peaks_df1), "peak_id")

#Cache & Persist
broadcast_df.show()

#Cache the members DataFrame
broadcast_df.cache()
broadcast_df.persist()

#Change NA data into null                                
broadcast_df = broadcast_df.na.fill('null')

#Write data to PostgreSQL
(
    broadcast_df
    .write
    .mode('overwrite')
    .jdbc(
        jdbc_url,
        'public.expeditions_merge',
        properties=jdbc_properties
    )
)