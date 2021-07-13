from django.db import models
from django.urls import reverse


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
    unicode_codes = models.TextField()

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