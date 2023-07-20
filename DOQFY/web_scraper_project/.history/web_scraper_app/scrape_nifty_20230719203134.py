from django.core.management.base import BaseCommand
from .scraper import scrape_nifty_50

class Command(BaseCommand):
    help = 'Scrape Nifty 50 data'

    def handle(self, *args, **options):
        scrape_nifty_50()
        self.stdout.write(self.style.SUCCESS('Successfully scraped Nifty 50 data'))
