from django.core.management.base import BaseCommand, CommandError
from emoji.models import EmojiWiki
import json
import traceback
import logging
LOG_FILENAME = '/home/nl/project/symbolsite/symbol_space/log_emojiwiki.txt'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
logging.debug('This message should go to the log file')



class Command(BaseCommand):
    help = 'Import du lieu tu emojis.wiki'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(options['path'][0]) as fin:
            data = json.load(fin)
        for entry in data:
            try:
                print(f"Entrizzzzzzzzzz : {entry['name']}\n")
                if entry.get('images'):
                    img = entry['images']
                else:
                    img = {}
                ejite = EmojiWiki.objects.create(
                    name=entry['name'],
                    emoji=entry['emoji'],
                    url=entry.get('url'),
                    slug=entry.get('url').split("/")[-2],

                    example = entry.get('example'),
                    combination = entry.get('combination'),
                    kaomoji = entry.get('kaomoji'),
                    unicode_info = entry.get('unicode_info'),
                    translation = entry.get('translation'),
                    related = entry.get('related_emoji'),


                    # IMAGES
                    img_apple = img.get('Apple'),
                    img_google = img.get('Google'),
                    img_microsoft = img.get('Microsoft'),
                    img_facebook = img.get('Facebook'),
                    img_messenger = img.get('Messenger'),
                    img_twitter = img.get('Twitter'),
                    img_whatsapp = img.get('WhatsApp'),
                    img_samsung = img.get('Samsung'),
                    img_lg = img.get('LG'),
                    img_htc = img.get('HTC'),
                    img_mozilla = img.get('Mozilla'),
                    img_softbank = img.get('SoftBank'),
                    img_au_by_kddi = img.get('au by KDDI'),
                    img_docomo = img.get('Docomo'),
                    img_openmoji = img.get('Openmoji'),
                )
            except:
                logging.exception('Got exception on main handler')
                raise

            ejite.save()

            self.stdout.write(self.style.SUCCESS(f"Inserted {ejite}"))
