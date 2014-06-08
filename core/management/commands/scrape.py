import datetime

from core.management.base import BaseCommand
from retriever import scraper

class Command(BaseCommand):

	def handle(self, args, options):

		print "handling scrape command"

		#the_day = datetime.date.today()
		the_day = datetime.date(2013,9,26)
		pdf = scraper.scrape(the_day)
		print(pdf)
