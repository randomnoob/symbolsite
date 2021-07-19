from django.db import models
from django.urls import reverse


class EmojiTerra(models.Model):
    """
    Class chua cac emoji crawl tu
    emojiterra.com
    """
    name = models.CharField(max_length=1000)
    emoji = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('emoji_detail', args=[str(self.slug)])
