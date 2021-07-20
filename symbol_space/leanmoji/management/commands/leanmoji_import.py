from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify
from leanmoji.models import Kaomoji
import json
import traceback


class Command(BaseCommand):
    help = 'Import du lieu'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(options['path'][0]) as fin:
            data = json.load(fin)
        for idx, entry in enumerate(data):
            try:
                print(f"Entrizzzzzzzzzz : {entry}\n")
                ejite = Kaomoji.objects.create(
                    name=entry.get('name'),
                    kaomoji=entry['face'],
                    url=entry.get('url'),
                    slug=slugify(entry.get('name'), allow_unicode=False)+f"-{idx}",
                    description=entry.get('description'),
                )
            except:
                traceback.print_exc()

            ejite.save()

            ejite_name = entry.get('name')
            self.stdout.write(self.style.SUCCESS(f"Inserted {ejite_name}"))
