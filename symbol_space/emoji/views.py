from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import EmojiTerra
import json

# Create your views here.

categories = ['Maps',  'Other Symbols',  'Writing',  'Reptiles',  'Mails',  'Monkey Faces',  'Small Animals',  'Transport: Ground',  'Other Places',  'Concerned Faces',  'Family',  'School & University',  'Subdivision Flags',  'Sleepy Faces',  'Flowers',  "Love & Valentine's Day",
              'Gestures',  'Medicine',  'Awards & Medals',  'Fruits',  'Alphanumeric Characters',  'Money',  'Asian Food',  'Autumn',  'Sportive People',  'Chinese New Year',  'Zodiac Signs',  'Common Flags',  'Signs',  'Tools',  'Audio & Video Symbols',  'Birds',  'Warnings',  'Halloween',  'Sky & Weather',  'Arrows',  'Shopping Emoji',  'Music',  'Hearts',  'Locks',  'Other Objects',  'Computer',  'Sound',  'Unwell (Sick) Faces',  'Birthday & Celebration & Party',  'Office',  'Arts & Crafts',  "Winter & Christmas & New Year's Eve",
              'Dishware',  'Prepared Food (Meals)',  'Transport: Water',  'Body Parts',  'Geometric Symbols',  'Mammals',  'Events',  '1 Keycaps',  'LGBT',  'Hands',  'Country Flags',  'People',  'Sweet Food & Sweets',  'Sports',  'Faces With Hand(s)',  'Drinks',  'Thanksgiving',  'Easter',  'Person: Symbol',  'Amphibians',  'Clothing',  'Neutral & Skeptical Faces',  'Faces With Accessories',  'TOP 100',  'Vegetables',  'Cat Faces',  'Summer',  'Musical Instruments',  'Fingers',  'Negative Faces',  'Resting People',  'Light & Video',  'Books & Papers',  'Hotel',  'Professions & Roles',  'Plants',  'Buildings',  'Seafood',  'Spring',  'Time',  'Faces With Affection',  'Religious Places',  'Ramadan',  'Science',  'Transport: Air',  'Fantasy & Fairy Tale',  'Emotions',  'Household',  'Geographic (Geo)',  'Gender',  'Activities & Hobbies',  'Costumed Faces',  'Marine Animals',  'Games',  'Religion',  'Phone',  'Smiling Faces',  'Faces With Tongue']

unicode_version_list = [
    "Unicode 13.0", "Unicode 12.0", "Unicode 11.0",
    "Unicode 10.0", "Unicode 9.0", "Unicode 8.0",
    "Unicode 7.0", "Unicode 6.1", "Unicode 6.0",
    "Unicode 5.2", "Unicode 5.1", "Unicode 4.1",
    "Unicode 4.0", "Unicode 3.2", "Unicode 3.0", "Unicode 1.1",
]


class EmojiTerraDetail(DetailView):
    model = EmojiTerra
    template_name = 'bsbay_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        if context.get('object'):
            unicode_codes = context.get('object').unicode_codes
            print(f" JSONIOZ : {unicode_codes}")
            jsonized = json.loads(str(unicode_codes))
            context['hexcodes'] = jsonized
        return context


class CategoryView(TemplateView):
    template_name = 'bsbay_category.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet
        catdict = {}
        for cat in categories:
            emoji_list = EmojiTerra.objects.filter(unicode_categories__contains=cat)
            catdict[cat] = emoji_list

        context['catdict'] = catdict
        return context


class UnicodeVersionView(TemplateView):
    template_name = 'bsbay_version.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet
        version_obj_list = {}
        for ver in unicode_version_list:
            version_objects = EmojiTerra.objects.filter(unicode_version__contains=ver)
            version_obj_list[ver] = version_objects

        context['versions'] = version_obj_list
        return context


# WILL BE REPLACED BY MANY-TO-MANY MODEL
# def single_category_view(request, category_name):
#     if category_name in categories:
#         emoji_in_cat = EmojiTerra.objects.filter(unicode_categories__contains=category_name)
#         context = {'bsbay_category': emoji_in_cat}
#         return response