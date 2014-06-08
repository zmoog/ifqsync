import os
import datetime
from core.management.base import BaseCommand

from archiver import get_client

class Command(BaseCommand):
	
	def handle(self, args, options):
		
		the_day = datetime.date.today()

		filename = the_day.strftime('ilfatto-%Y%m%d.pdf')


		client = get_client(options)


		print "Searching for %s in the Dropbox archive .. " % (filename)
		result = client.search('/Il Fatto Quotidiano', filename)

		if not result:
			
			print "%s does not exists (yet)" % (filename)

		else:
			print 'already present: %s' % (result)
