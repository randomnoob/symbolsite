import json
import random
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.shortcuts import render
from django.db.models import Max, Min
from .models import Category, EmojiTerra, EmojiWiki
from .utils import get_featured_links

# Create your views here.


def get_random_emoji(num=15):
    """
    get random 10 emoji from db
    https://books.agiliq.com/projects/django-orm-cookbook/en/latest/random.html
    """
    # emoji = list(EmojiTerra.objects.all())
    # chosen_emoji = []
    # while len(chosen_emoji) < 10:
    #     chosen_emoji.append(random.choice(emoji))
    # print(f"BUXX {chosen_emoji}")
    # return chosen_emoji

    max_id = EmojiTerra.objects.all().aggregate(max_id=Max("id"))['max_id']
    min_id = EmojiTerra.objects.all().aggregate(min_id=Min("id"))['min_id']
    rand_pk = [random.randint(min_id, max_id) for x in range(1, num)]
    emoji = EmojiTerra.objects.filter(id__in=rand_pk)
    return emoji





class HomeView(TemplateView):
    template_name= 'bsbay_home.html'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context= super().get_context_data(**kwargs)
        # Add in a QuerySet
        context['featured']= get_featured_links()
        return context


class EmojiTerraDetail(DetailView):
    model= EmojiTerra
    template_name= 'bsbay_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context= super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        if context.get('object'):
            unicode_codes= context.get('object').unicode_codes
            jsonized= json.loads(str(unicode_codes))
            context['hexcodes']= jsonized
            context['random_emoji']= get_random_emoji()
            emoji_wiki = EmojiWiki.objects.filter(emoji=context.get('object').emoji).first()
            context['emoji_wiki'] = emoji_wiki
            print("*/**************Shit found!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return context


class CategoryView(DetailView):
    template_name= 'bsbay_category.html'
    model= Category

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context= super().get_context_data(**kwargs)
        # Add in a QuerySet
        context['random_emoji']= get_random_emoji()
        return context


class CategoryListView(ListView):
    model= Category
    template_name= 'bsbay_category_all.html'
