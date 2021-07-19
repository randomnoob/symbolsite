from django.db import models
from django.urls import reverse
from emoji.models import EmojiTerra


class Codepoints(models.Model):
    """
    The codepoint model
    """
    name = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True)
    emoji = models.ForeignKey(EmojiTerra,
                              on_delete=models.CASCADE,
                              default=None,
                              blank=True,
                              null=True
                              )

    def __str__(self):
        return self.slug
