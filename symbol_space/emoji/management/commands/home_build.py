from django.core.management.base import BaseCommand
from emoji.models import EmojiTerra, Category
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
import json
import traceback


class Command(BaseCommand):
    help = 'Import du lieu vao home'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(options['path'][0]) as fin:
            data = json.load(fin)
        for catename, emojilist in data.items():
                print(f"Entrizzzzzzzzzz : {catename}\n")
                slug = slugify(catename, allow_unicode=False)
                cate = Category.objects.update_or_create(
                    slug=slug,
                    defaults={
                        'name':catename,
                        'slug':slug,
                    },
                )
                print(f"Cate{cate}")
                for emocode in emojilist:
                    print(f"Saving {emocode}")
                    try:
                        emo = EmojiTerra.objects.get(emoji=emocode)
                        emo.category.add(cate[0])
                        emo.save()
                        print(f"Saved {emo}")
                    except:
                        traceback.print_exc()
                        pass


            # self.stdout.write(self.style.SUCCESS(f"Inserted {ejite_name}"))
