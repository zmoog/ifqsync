import os

# Include the Dropbox SDK libraries
from dropbox import client, session # ,rest

import settings

# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = 'dropbox'


def get_client(options):

	current_session = session.DropboxSession(settings.API_KEY, settings.API_SECRET, ACCESS_TYPE)

	# We will use the OAuth token we generated already. The set_token API
	# accepts the oauth_token and oauth_token_secret as inputs.
	current_session.set_token(settings.ACCESS_TOKEN_KEY, settings.ACCESS_TOKEN_SECRET)

	return client.DropboxClient(current_session)
