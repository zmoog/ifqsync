import os
import datetime
from core.management.base import BaseCommand

from archiver import get_client
from retriever import scraper

class Command(BaseCommand):
	
	def handle(self, args, options):
		
		the_day = datetime.date.today()


		pdf = scraper.scrape(the_day)

