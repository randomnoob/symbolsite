from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify
from leanmoji.models import Kaomoji, KTag
import json
import traceback
import ast
import itertools


class Command(BaseCommand):
    help = 'Import du lieu'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(options['path'][0]) as fin:
            data = json.load(fin)


        plaintext_tags = [entry['keyword'] for entry in data]
        flatten_tags = list(itertools.chain(*plaintext_tags))
        unique_tags = list(set(flatten_tags))
        for idx, tagname in enumerate(unique_tags):
            dbtag = KTag.objects.create(
                name = tagname,
                slug = slugify(tagname, allow_unicode=False)+f"-{idx}",
            )
            dbtag.save()
            print(f"Saved {dbtag}")
        
            

        filtered = []
        for entry in data:
            page = entry['from_page'].split("&page=")[-1]
            if ast.literal_eval(page)<=215:
                if "U+" not in entry['url']:
                    filtered.append(entry)

        for idx, entry in enumerate(filtered):
            try:
                print(f"Entrizzzzzzzzzz : {entry}\n")
                ejite = Kaomoji.objects.create(
                    name=entry.get('name'),
                    kaomoji=entry['face'],
                    url="https://www.fastemoji.com/" + entry.get('url'),
                    slug=slugify(entry.get('name'), allow_unicode=False)+f"-{idx}",
                    description='',
                )
                for tagname in entry['keyword']:
                    the_tag = KTag.objects.get(name=tagname)
                    ejite.tag.add(the_tag)
                    print(f"Added tag {the_tag}")
            except:
                traceback.print_exc()

            ejite.save()

            ejite_name = entry.get('name')
            self.stdout.write(self.style.SUCCESS(f"Inserted {ejite_name}"))
