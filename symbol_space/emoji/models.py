from django.db import models
from django.urls import reverse
import json
import ast


class Category(models.Model):
    """
    The category/tag model for the main emojis
    """
    name = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.slug


class EmojiTerra(models.Model):
    """
    Class chua cac emoji crawl tu
    emojiterra.com
    """
    name = models.CharField(max_length=1000)
    emoji = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    unicode_shortname = models.CharField(max_length=1000)
    unicode_keywords = models.CharField(max_length=1000)
    unicode_categories = models.CharField(max_length=1000)
    unicode_codepoints = models.CharField(max_length=1000)
    unicode_version = models.CharField(max_length=1000)
    unicode_codes = models.TextField(blank=True, null=True)

    # SUPPORT
    android_4_4_kitkat = models.CharField(max_length=1000)
    android_5_1_lollipop = models.CharField(max_length=1000)
    android_6_0_1_marshmallow = models.CharField(max_length=1000)
    android_7_1_1_nougat = models.CharField(max_length=1000)
    android_8_0_oreo = models.CharField(max_length=1000)
    android_9_0_pie = models.CharField(max_length=1000)
    android_10_0 = models.CharField(max_length=1000)
    android_11_0 = models.CharField(max_length=1000)
    fxemojis_1_7_9 = models.CharField(max_length=1000)
    openmoji_12_2 = models.CharField(max_length=1000)
    twemoji_2_3 = models.CharField(max_length=1000)
    twemoji_12_1_5 = models.CharField(max_length=1000)
    twemoji_13_0 = models.CharField(max_length=1000)

    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('emoji_detail_slug', args=[str(self.id)])


class EmojiWiki(models.Model):
    """
    Class chua cac emoji crawl tu
    emojis.wiki
    """
    name = models.CharField(max_length=1000)
    emoji = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    intro = models.TextField(blank=True, null=True)
    example = models.TextField(blank=True, null=True)
    combination = models.TextField(blank=True, null=True)
    kaomoji = models.TextField(blank=True, null=True)
    unicode_info = models.TextField(blank=True, null=True)
    translation = models.TextField()
    related = models.TextField(blank=True, null=True)

    # IMAGES
    img_apple = models.CharField(max_length=1000, blank=True, null=True)
    img_google = models.CharField(max_length=1000, blank=True, null=True)
    img_microsoft = models.CharField(max_length=1000, blank=True, null=True)
    img_facebook = models.CharField(max_length=1000, blank=True, null=True)
    img_messenger = models.CharField(max_length=1000, blank=True, null=True)
    img_twitter = models.CharField(max_length=1000, blank=True, null=True)
    img_whatsapp = models.CharField(max_length=1000, blank=True, null=True)
    img_samsung = models.CharField(max_length=1000, blank=True, null=True)
    img_lg = models.CharField(max_length=1000, blank=True, null=True)
    img_htc = models.CharField(max_length=1000, blank=True, null=True)
    img_mozilla = models.CharField(max_length=1000, blank=True, null=True)
    img_softbank = models.CharField(max_length=1000, blank=True, null=True)
    img_au_by_kddi = models.CharField(max_length=1000, blank=True, null=True)
    img_docomo = models.CharField(max_length=1000, blank=True, null=True)
    img_openmoji = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.slug

    def show_example(self):
        return self.show_object('example')

    def show_combination(self):
        return self.show_object('combination')

    def show_kaomoji(self):
        return self.show_object('kaomoji')

    def show_translation(self):
        return self.show_object('translation')

    def show_related(self):
        return self.show_object('related')

    def show_object(self, obj_name):
        if not hasattr(self, obj_name):
            return None
        try:
            obj = ast.literal_eval(getattr(self, obj_name))
            if not obj:
                obj = []
            return obj
        except:
            return []

    def show_platforms(self):
        platforms = {
            "Apple": getattr(self, "img_apple"),
            "Google": getattr(self, "img_google"),
            "Microsoft": getattr(self, "img_microsoft"),
            "Facebook": getattr(self, "img_facebook"),
            "Messenger": getattr(self, "img_messenger"),
            "Twitter": getattr(self, "img_twitter"),
            "WhatsApp": getattr(self, "img_whatsapp"),
            "Samsung": getattr(self, "img_samsung"),
            "LG": getattr(self, "img_lg"),
            "HTC": getattr(self, "img_htc"),
            "Mozilla": getattr(self, "img_mozilla"),
            "SoftBank": getattr(self, "img_softbank"),
            "au by KDDI": getattr(self, "img_au_by_kddi"),
            "Docomo": getattr(self, "img_docomo"),
            "Openmoji": getattr(self, "img_openmoji"),
        }
        return platforms
