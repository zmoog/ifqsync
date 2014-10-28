import os

# Get your app key and secret from the Dropbox developer website

APP_KEY = os.environ['IFQSYNC_DROPBOX_APP_KEY']
APP_SECRET = os.environ['IFQSYNC_DROPBOX_APP_SECRET']
ACCESS_TOKEN_KEY = os.environ['IFQSYNC_DROPBOX_ACCESS_TOKEN_KEY']
ACCESS_TOKEN_SECRET = os.environ['IFQSYNC_DROPBOX_ACCESS_TOKEN_SECRET']

IFQ_USERNAME = os.environ['IFQSYNC_IFQ_USERNAME']
IFQ_PASSWORD = os.environ['IFQSYNC_IFQ_PASSWORD']

TMP_PATH = os.environ['IFQSYNC_TMP_PATH']

TARGET_FILENAME_PATTERN = 'ilfatto-%Y%m%d.pdf'
ROOT_FOLDER = '/Il Fatto Quotidiano'
