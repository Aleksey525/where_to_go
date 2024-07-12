from django.core.management.base import BaseCommand
from places.fill_up_db import main
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, help='json-file url')

    def handle(self, *args, **options):
        json_url = options.get('json_url')
        main(json_url)



