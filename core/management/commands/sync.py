import os
import datetime
from core.management.base import BaseCommand

from archiver import get_client
from retriever import scraper

class Command(BaseCommand):
	
	def handle(self, args, options):
		
		the_day = datetime.date.today()
		#the_day = datetime.date(2014,4,26)

		filename = the_day.strftime('ilfatto-%Y%m%d.pdf')

		print "handling: %s" % (filename)

		client = get_client(options)


		result = client.search('/Il Fatto Quotidiano', filename)

		if not result:
			
			print "%s does not exists (yet)" % (filename)

			#scraper = get_scraper(options)

			pdf = scraper.scrape(the_day)
		
			if pdf:
				client.put_file('/Il Fatto Quotidiano/%s' % filename, open(pdf))
			else:
				print "This issue is not yet availabe."


		else:
			print 'already present: %s' % (result)
