from pyspark.sql import SparkSession
from pyspark.sql.functions import col

S3_DATA_SOURCE_PATH = 's3://mybigdataapp/dataset/Google-Playstore.csv'
S3_DATA_OUTPUT_PATH = 's3://mybigdataapp/data-output'

def main():
    spark = SparkSession.builder.appName('mybigdataapp').getOrCreate()
    all_data = spark.read.csv(S3_DATA_SOURCE_PATH, header=True)
    print('Total number of records in the source data: %s' % all_data.count())
    selected_data = all_data.where((col('Category') == 'Education') & (col('Rating') > 3.00))
    print('Number of Education apps with rating over 3: %s' % selected_data.count())
    selected_data.write.mode('overwrite').csv(S3_DATA_OUTPUT_PATH)
    print('Selected data was successfully saved to s3: %s' % S3_DATA_OUTPUT_PATH)
    
if __name__ == '__main__':
    main()
