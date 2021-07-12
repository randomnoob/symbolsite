import json
import itertools
import traceback
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from django.utils.text import slugify
from emoji.models import EmojiTerra, Category

unicode_version_list = [
    "Unicode 13.0", "Unicode 12.0", "Unicode 11.0",
    "Unicode 10.0", "Unicode 9.0", "Unicode 8.0",
    "Unicode 7.0", "Unicode 6.1", "Unicode 6.0",
    "Unicode 5.2", "Unicode 5.1", "Unicode 4.1",
    "Unicode 4.0", "Unicode 3.2", "Unicode 3.0", "Unicode 1.1",
]


class Command(BaseCommand):
    help = 'Tao Category va set category cho Emoji'

    def handle(self, *args, **options):
        try:
            all_emojis = EmojiTerra.objects.all()
            category_list = [x.unicode_categories.split(",") for x in all_emojis]
            category_chained = list(itertools.chain(*category_list))
            category_chained = list(set([x.strip() for x in category_chained]))

            for cat in category_chained:
                cat_slug = slugify(cat, allow_unicode=True)
                print (f"Categori : {cat}")
                db_cat = Category.objects.get_or_create(name=cat,
                            slug=cat_slug+"-emoji")
                
                emoji_list = EmojiTerra.objects.filter(unicode_categories__contains=cat)
                print (f"Emojilist : {emoji_list}")
                for emo in emoji_list:
                    cat_obj = db_cat[0]
                    emo.category.add(cat_obj)
                    emo.save()
                
                self.stdout.write(self.style.SUCCESS(f"Inserted {cat}"))
            # INSERT UNICODE VERSION
            for cat in unicode_version_list:
                cat_slug = slugify(cat, allow_unicode=True)
                print (f"Categori : {cat}")
                db_cat = Category.objects.get_or_create(name=cat,
                            slug=cat_slug+"-emoji")
                
                emoji_list = EmojiTerra.objects.filter(unicode_version__contains=cat)
                print (f"Emojilist : {emoji_list}")
                for emo in emoji_list:
                    cat_obj = db_cat[0]
                    emo.category.add(cat_obj)
                    emo.save()
                
                self.stdout.write(self.style.SUCCESS(f"Inserted {cat}"))

        except:
            traceback.print_exc()
        

            # self.stdout.write(self.style.SUCCESS(f"Inserted {ejite_name}"))
