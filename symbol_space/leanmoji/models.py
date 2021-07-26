from django.db import models
from django.urls import reverse

class KCategory(models.Model):
    """
    The category model
    """
    name = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True)
    meta_html = models.TextField(null=True)


    def __str__(self):
        return self.slug

class KTag(models.Model):
    """
    The category model
    """
    name = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True)
    meta_html = models.TextField(null=True)

    def __str__(self):
        return self.slug


class Kaomoji(models.Model):
    """
    Class chua cac emoji crawl tu
    emojiterra.com
    """
    name = models.CharField(max_length=1000, null=True)
    kaomoji = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000, null=True)
    slug = models.SlugField(unique=True)
    keywords = models.TextField(null=True)
    description = models.TextField(null=True)

    category = models.ManyToManyField(KCategory)
    tag = models.ManyToManyField(KTag)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('emo_detail', args=[str(self.slug)])
