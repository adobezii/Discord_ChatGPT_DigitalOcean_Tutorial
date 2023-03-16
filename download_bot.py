import boto3
import os

BUCKET_NAME = 'cloudspace32'
FOLDER_NAME = 'discord_chatGPT'
LOCAL_FOLDER = '/root/discord_chatGPT'

s3 = boto3.resource('s3')

bucket = s3.Bucket(BUCKET_NAME)

for obj in bucket.objects.filter(Prefix=FOLDER_NAME):
    if not os.path.exists(os.path.dirname(LOCAL_FOLDER + os.sep + obj.key)):
        os.makedirs(os.path.dirname(LOCAL_FOLDER + os.sep + obj.key))
    bucket.download_file(obj.key, LOCAL_FOLDER + os.sep + obj.key)
