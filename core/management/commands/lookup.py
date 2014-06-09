import os
import datetime
from core.management.base import BaseCommand

from archiver import get_client

from settings import TARGET_FILENAME_PATTERN
from settings import ROOT_FOLDER as TARGET_FOLDER


class Command(BaseCommand):

	def handle(self, args, options):

		target_date = options.target_date

		filename = target_date.strftime(TARGET_FILENAME_PATTERN)

		client = get_client(options)

		print "Searching for %s in the Dropbox archive .. " % (filename)

		result = client.search(TARGET_FOLDER, filename)

		if not result:
			print "%s does not exists (yet)" % (filename)
		else:
			print 'already present: %s' % (result)

		return result
