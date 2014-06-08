import os
import datetime
from core.management.base import BaseCommand

from archiver import get_client
from retriever import scraper

ROOT_FOLDER = '/Il Fatto Quotidiano'
TARGET_FILENAME_PATTERN = 'ilfatto-%Y%m%d.pdf'

class Command(BaseCommand):

	def handle(self, args, options):

		target_day = datetime.date.today()
		# target_day = datetime.date(2014,6,6)

		target_filename = target_day.strftime(TARGET_FILENAME_PATTERN)

		print "Looking for %s in the Dropbox archive .. " % (target_filename)

		client = get_client(options)


		result = client.search(ROOT_FOLDER, target_filename)

		if not result:

			print "File %s does not exists (yet)" % (target_filename)


			local_filename = scraper.scrape(target_day)
		
			if local_filename:
				response = client.put_file('%s/%s' % (ROOT_FOLDER, target_filename), open(local_filename))
				print "Original: ", os.stat(local_filename)
				print "Uploaded: ", response
			else:
				print "This issue is not yet availabe."


		else:
			print 'File %s is already present: %s' % (result)
