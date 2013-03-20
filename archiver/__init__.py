import os

# Include the Dropbox SDK libraries
from dropbox import client, rest, session

# Get your app key and secret from the Dropbox developer website
APP_KEY = os.environ['IFQSYNC_DROPBOX_API_KEY']
APP_SECRET = os.environ['IFQSYNC_DROPBOX_API_SECRET']

# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = 'dropbox'


def get_client(options):

	#print "tyye", dir(options)

	sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

	# We will use the OAuth token we generated already. The set_token API 
	# accepts the oauth_token and oauth_token_secret as inputs.
	sess.set_token(options.access_token_key, options.access_token_secret)

	return client.DropboxClient(sess)
