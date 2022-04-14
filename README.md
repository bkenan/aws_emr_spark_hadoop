# Big Data Processing with Spark and Hadoop using AWS EMR (Elastic MapReduce)

This repo performs a simple big data engineering task on Google Play Store App data using AWS S3 bucket + EMR + Spark and Hadoop

[The dataset can be found here](https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps)


General workflow:

1. Create S3 bucket and upload the dataset 
2. Create EMR cluster and add SSH+IP into the inbound security rules
3. [Create SSH key](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html)
4. Connect to the Master Node Using SSH using 
5. Run spark-submit main.py after creating the script



The key outcome is that total number of records in the source dataset is 1,048,575 while the number of Education apps with rating over 3 is 54,158
Also, I've saved the list of those apps within "data outputs" folder into S3 bucket. 

Demo screenshots:

![EMR](https://user-images.githubusercontent.com/53462948/163347219-3a80ff31-7be1-49c6-813a-13344346bf1f.png)

![s3](https://user-images.githubusercontent.com/53462948/163347265-03f0e962-ea71-4554-86a0-1c16e5e31210.png)

![partial outcome](https://user-images.githubusercontent.com/53462948/163347313-ed5cab29-e651-4fa4-b79e-0afb7487918e.png)
