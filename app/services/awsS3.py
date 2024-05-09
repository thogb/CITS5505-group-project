from flask import Flask
from flask_caching import Cache
import boto3

class AWSS3:
    def __init__(self, app: Flask = None):
        if app is not None:
            self.create_from_app(app)

    def create_from_app(self, app: Flask, cache: Cache):
        self.cache = cache
        self.client = boto3.client(
            's3',
            aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY']
        )
        self.bucket_name = app.config['AWS_S3_BUCKET_NAME']

    def upload_file(self, file, object_name):
        self.client.upload_fileobj(file, self.bucket_name, object_name)

    def generate_presigned_url(self, object_name, expiration_seconds=3600):
        cached_url_string = self.cache.get(object_name);

        if cached_url_string is not None:
            return cached_url_string

        url_string =  self.client.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': self.bucket_name,
                'Key': object_name
            },
            ExpiresIn=expiration_seconds
        )

        self.cache.set(object_name, url_string, expiration_seconds)
    
        return url_string