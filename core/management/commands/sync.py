import os
import datetime
from core.management.base import BaseCommand

from archiver import get_client
from retriever import scraper

from settings import TARGET_FILENAME_PATTERN, ROOT_FOLDER

class Command(BaseCommand):

	def handle(self, args, options):

		#if options.target_date:
		target_date = options.target_date
		#else:
		#	target_date = datetime.date.today()

		target_filename = target_date.strftime(TARGET_FILENAME_PATTERN)

		print "Looking for %s in the Dropbox archive .. " % (target_filename)

		client = get_client(options)


		result = client.search(ROOT_FOLDER, target_filename)

		if not result:

			print "File %s does not exists (yet)" % (target_filename)


			local_filename = scraper.scrape(target_date)

			if local_filename:
				response = client.put_file('%s/%s' % (ROOT_FOLDER, target_filename), open(local_filename))
				print "Original: ", os.stat(local_filename)
				print "Uploaded: ", response
			else:
				print "This issue is not yet availabe."


		else:
			print 'File %s is already present: %s' % (target_filename, result)
