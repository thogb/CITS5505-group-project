import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET KEY'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') or "AKIAQRUNCJR6OXQKZHBP"
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') or "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"
    AWS_S3_BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME') or "dreamers-market"