# import json
# import random
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
# from django.views.generic import TemplateView
# from django.shortcuts import render

# class CategoryListView(ListView):
#     model= Category
#     template_name= 'bsbay_category_all.html'

import traceback
import itertools
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
from django.views.generic.list import ListView

from leanmoji.models import Kaomoji
from .utils import link, p, table, li, card, heading2, free_wrap

####################################################
# HELPER FUNCTIONS
####################################################

def default_sidebar():
    recent = Kaomoji.objects.all()[:10]
    h2_kao = heading2("Recent kaomoji", class_='text-center py-2')
    recent_html = [link(href=reverse('emo_detail', args=[x.slug]), anchor=f"{x.kaomoji} {x.name}") for x in recent]
    recent_list_html = li(recent_html, class_="  card-text list-unstyled  text-center")
    view_all = link(href="/emo/all", anchor="View all kaomoji", class_="btn btn-block btn-sm btn-secondary")

    h2_dance = heading2("Dance kaomoji", class_='text-center py-2')
    dance = Kaomoji.objects.filter(name__contains="dance")[:15]
    dance_html = [link(href=reverse('emo_detail', args=[x.slug]), anchor=x.kaomoji) for x in dance]
    dance_list_html = li(dance_html, class_="  card-text list-unstyled  text-center")
    
    view_more = link(href="/emo/c/Dance", anchor="View more", class_="btn btn-block btn-sm btn-light")

    sidebar = h2_kao + recent_list_html + view_all + h2_dance + dance_list_html + view_more
    return sidebar

def query_latest():
    recent = Kaomoji.objects.all().order_by('-id')[:20]
    head2 = heading2("Popular today", class_='text-center py-3')
    recent_html = [link(href=reverse('emo_detail', args=[x.slug]), anchor=f"{x.kaomoji} {x.name}") for x in recent]
    return head2+li(recent_html, class_="text-center list-unstyled") 


def query_nearby(main_object):
    main_pk = main_object.pk
    try:
        nearby = [Kaomoji.objects.get(pk=x) for x in range(main_pk-7, main_pk+7)]
    except Kaomoji.DoesNotExist:
        nearby = Kaomoji.objects.all()[:15]
    head2 = heading2("Related Kaomoji", class_='text-center py-3')
    nearby_html = [link(href=reverse('emo_detail', args=[x.slug]), anchor=f"{x.kaomoji} {x.name}") for x in nearby]
    return head2 + li(nearby_html, class_="text-center  list-unstyled")


####################################################
# ACTUAL VIEW FUNCTIONS
####################################################

def detail(request, slug):
    try:
        print(f"Finding slug : {slug}")
        obj = Kaomoji.objects.get(slug=slug)
        print(f"xzzzzz: {obj}")
        title = obj.kaomoji + " " + obj.name + " Lenny Face"
        if not obj.name:
            title += " " + obj.description + " Lenny Face"

        
        kaomoji_copy = render_to_string('partials/copy-box.html', {'copy_value': obj.kaomoji})
        kaomoji_box = free_wrap(kaomoji_copy, wrapper='div', class_="main-box")

        kaomoji_description = render_to_string('partials/detail_paragraph.html',\
                context={'name': obj.name, 'emoji': obj.kaomoji, 'category': obj.description})
        desc = kaomoji_box + p(kaomoji_description, class_="text-left")
        obj_card = card(title=obj.name, body=desc)
        content = obj_card + query_nearby(obj) + query_latest()
    except Kaomoji.DoesNotExist:
        raise Http404("Kaomoji does not exist")
    return render(request, 'bsbay_base.html', {'title': title, 'content': content, 'sidebar':default_sidebar()})

def homeview(request):
    try:
        obj = Kaomoji.objects.all().order_by('-id')[:40]
        title = "Collection of most used Lenny faces and Text Emoticons"
        
        obj_html = [link(href=reverse('emo_detail', args=[x.slug]), anchor=f"{x.kaomoji} {x.name}") for x in obj]
        obj_list_html = free_wrap(li(obj_html), wrapper='div', class_="text-center")

        content = obj_list_html + query_latest()
    except Kaomoji.DoesNotExist:
        raise Http404("Kaomoji does not exist")
    return render(request, 'bsbay_base.html', {'title': title, 'content': content, 'sidebar':default_sidebar()})


def cateview(request, category):
    try:
        obj1 = Kaomoji.objects.filter(name__contains=category)
        obj2 = Kaomoji.objects.filter(description__contains=category)
        obj = itertools.chain(obj1, obj2)
        title = f"{category.title()} Lenny faces and Text Emoticons"
        
        obj_html = []
        idx = 0
        for x in obj:
            obj_html.append(link(href=reverse('emo_detail', args=[x.slug]), anchor=f"{x.kaomoji} {x.name}"))
            idx += 1
            if idx >= 30:
                break

        obj_list_html = free_wrap(li(obj_html), wrapper='div', class_="text-center")

        content = obj_list_html
    except Kaomoji.DoesNotExist:
        raise Http404("Kaomoji does not exist")
    return render(request, 'bsbay_base.html', {'title': title, 'content': content, 'sidebar':default_sidebar()})



class KaomojiListView(ListView):
    model= Kaomoji
    template_name= 'bsbay_kaomoji_all.html'
    paginate_by = 20
