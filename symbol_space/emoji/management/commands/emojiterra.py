from django.core.management.base import BaseCommand, CommandError
from emoji.models import EmojiTerra
import json
import traceback


class Command(BaseCommand):
    help = 'Import du lieu'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(options['path'][0]) as fin:
            data = json.load(fin)
        for entry in data:
            try:
                print(f"Entrizzzzzzzzzz : {entry['meaning']}\n")
                ejite = EmojiTerra.objects.create(
                    name=entry['meaning']['Short name:'].capitalize(),
                    # TAKE EMOJI FROM ANOTHER FIELD BECAUSE ORIGINAL ONE IS CORRUPTED
                    emoji=entry['emoji'],
                    url=entry['url'],
                    slug=entry['url'].split("/")[-2],
                    unicode_shortname=entry['meaning']['Short name:'],
                    unicode_keywords=entry['meaning']['Keywords:'],
                    unicode_categories=entry['meaning']['Categories:'],
                    # REPLACE TO CLEAN THE FIELD
                    unicode_codepoints=entry['unicode_data']['Unicode Code Point(s)'].replace("Variation Selector", ", Variation Selector"),
                    # REPLACE TO CLEAN THE FIELD
                    unicode_version=entry['unicode_data']['Listed in:'].replace("Unicode", ", Unicode"),
                    unicode_codes=json.dumps(entry['emoji_codes']),

                    android_4_4_kitkat=entry['support']['Android 4.4 KitKat'],
                    android_5_1_lollipop=entry['support']['Android 5.1 Lollipop'],
                    android_6_0_1_marshmallow=entry['support']['Android 6.0.1 Marshmallow'],
                    android_7_1_1_nougat=entry['support']['Android 7.1.1 Nougat'],
                    android_8_0_oreo=entry['support']['Android 8.0 Oreo'],
                    android_9_0_pie=entry['support']['Android 9.0 Pie'],
                    android_10_0=entry['support']['Android 10.0'],
                    android_11_0=entry['support']['Android 11.0'],
                    fxemojis_1_7_9=entry['support']['FxEmojis 1.7.9'],
                    openmoji_12_2=entry['support']['OpenMoji 12.2'],
                    twemoji_2_3=entry['support']['Twemoji 2.3'],
                    twemoji_12_1_5=entry['support']['Twemoji 12.1.5'],
                    twemoji_13_0=entry['support']['Twemoji 13.0'],
                )
            except:
                traceback.print_exc()

            ejite.save()

            ejite_name = entry['meaning']['Short name:'].capitalize()
            self.stdout.write(self.style.SUCCESS(f"Inserted {ejite_name}"))
