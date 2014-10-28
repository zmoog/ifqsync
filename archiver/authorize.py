import os

# Include the Dropbox SDK libraries
from dropbox import client, rest, session

# Get your app key and secret from the Dropbox developer website
APP_KEY = os.environ['IFQSYNC_DROPBOX_APP_KEY'] 
APP_SECRET = os.environ['IFQSYNC_DROPBOX_APP_SECRET']

# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = 'dropbox'
sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

request_token = sess.obtain_request_token()

url = sess.build_authorize_url(request_token)
print "url:", url
print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
raw_input()

access_token = sess.obtain_access_token(request_token)
print "access_token:", access_token.key, access_token.secret


client = client.DropboxClient(sess)
print "linked account:", client.account_info()
