import os

# Include the Dropbox SDK libraries
from dropbox import client, rest, session

# Get your app key and secret from the Dropbox developer website
APP_KEY = os.environ['IFQSYNC_DROPBOX_API_KEY']
APP_SECRET = os.environ['IFQSYNC_DROPBOX_API_SECRET']

# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = 'dropbox'
sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

ACCESS_TOKEN_KEY = os.environ['IFQSYNC_DROPBOX_ACCESS_TOKEN_KEY']
ACCESS_TOKEN_SECRET = os.environ['IFQSYNC_DROPBOX_ACCESS_TOKEN_SECRET']


# We will use the OAuth token we generated already. The set_token API 
# accepts the oauth_token and oauth_token_secret as inputs.
sess.set_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)


# request_token = sess.obtain_request_token()
# 
# url = sess.build_authorize_url(request_token)
# print "url:", url
# print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
# raw_input()
# 
# access_token = sess.obtain_access_token(request_token)
# print "access_token:", access_token.oauth_token, access_token.oauth_token_secret


client = client.DropboxClient(sess)
print "linked account:", client.account_info()


# Let's upload a file!
f = open(os.path.join(os.environ['IFQSYNC_TMP_PATH'], 'ilfatto-20130318.pdf'))
response = client.put_file('/Il Fatto Quotidiano/ilfatto-20130318.pdf', f)
print "uploaded:", response
