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
                print(f"Entrizzzzzzzzzz : {entry['data']['meaning']}\n")
                ejite = EmojiTerra.objects.create(
                    name=entry['name'],
                    # TAKE EMOJI FROM ANOTHER FIELD BECAUSE ORIGINAL ONE IS CORRUPTED
                    emoji=entry['data']['unicode_data']['Unicode Code Point(s)'].split(":")[0],
                    url=entry['link'],
                    slug=entry['link'].split("/")[-2],
                    unicode_shortname=entry['data']['meaning']['Short name:'],
                    unicode_keywords=entry['data']['meaning']['Keywords:'],
                    unicode_categories=entry['data']['meaning']['Categories:'],
                    # REPLACE TO CLEAN THE FIELD
                    unicode_codepoints=entry['data']['unicode_data']['Unicode Code Point(s)'].replace("Variation Selector", ", Variation Selector"),
                    # REPLACE TO CLEAN THE FIELD
                    unicode_version=entry['data']['unicode_data']['Listed in:'].replace("Unicode", ", Unicode"),
                    unicode_codes=json.dumps(entry['data']['emoji_codes']),

                    android_4_4_kitkat=entry['data']['support']['Android 4.4 KitKat'],
                    android_5_1_lollipop=entry['data']['support']['Android 5.1 Lollipop'],
                    android_6_0_1_marshmallow=entry['data']['support']['Android 6.0.1 Marshmallow'],
                    android_7_1_1_nougat=entry['data']['support']['Android 7.1.1 Nougat'],
                    android_8_0_oreo=entry['data']['support']['Android 8.0 Oreo'],
                    android_9_0_pie=entry['data']['support']['Android 9.0 Pie'],
                    android_10_0=entry['data']['support']['Android 10.0'],
                    android_11_0=entry['data']['support']['Android 11.0'],
                    fxemojis_1_7_9=entry['data']['support']['FxEmojis 1.7.9'],
                    openmoji_12_2=entry['data']['support']['OpenMoji 12.2'],
                    twemoji_2_3=entry['data']['support']['Twemoji 2.3'],
                    twemoji_12_1_5=entry['data']['support']['Twemoji 12.1.5'],
                    twemoji_13_0=entry['data']['support']['Twemoji 13.0'],
                )
            except:
                traceback.print_exc()

            ejite.save()

            ejite_name = entry['name']
            self.stdout.write(self.style.SUCCESS(f"Inserted {ejite_name}"))
