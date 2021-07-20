# import json
# import random
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
# from django.views.generic import TemplateView
# from django.shortcuts import render

# class CategoryListView(ListView):
#     model= Category
#     template_name= 'bsbay_category_all.html'


from django.http import Http404
from django.shortcuts import render
from leanmoji.models import Kaomoji
from django.template.loader import render_to_string
from .utils import link, p, table, li, card, heading2, free_wrap

def default_sidebar():
    recent = Kaomoji.objects.all()[:10]
    h2_kao = heading2("Recent kaomoji", class_='text-center py-2')
    recent_html = [link(href=f"/emo/{x.slug}", anchor=f"{x.kaomoji} {x.name}") for x in recent]

    h2_dance = heading2("Dance kaomoji", class_='text-center py-2')
    dance = Kaomoji.objects.filter(name__contains="dance")
    dance_html = [link(href=f"/emo/{x.slug}", anchor=x.kaomoji) for x in dance]
    sidebar = h2_kao + li(recent_html) + h2_dance + li(dance_html)
    return sidebar

def query_latest():
    recent = Kaomoji.objects.all()[:20]
    head2 = heading2("Popular today", class_='text-center py-3')
    recent_html = [link(href=f"/emo/{x.slug}", anchor=f"{x.kaomoji} {x.name}") for x in recent]
    return head2+li(recent_html, class_="text-center list-unstyled")


def query_nearby(main_object):
    main_pk = main_object.pk
    nearby = [Kaomoji.objects.get(pk=x) for x in range(main_pk-7, main_pk+7)]
    head2 = heading2("Related Kaomoji", class_='text-center py-3')
    nearby_html = [link(href=f"/emo/{x.slug}", anchor=f"{x.kaomoji} {x.name}") for x in nearby]
    return head2 + li(nearby_html, class_="text-center  list-unstyled")

def detail(request, slug):
    try:
        obj = Kaomoji.objects.get(slug=slug)
        title = obj.name

        
        kaomoji_copy = render_to_string('partials/copy-box.html', {'copy_value': obj.kaomoji})
        kaomoji_box = free_wrap(kaomoji_copy, wrapper='div', class_="main-box")


        desc = kaomoji_box + p(obj.description)
        obj_card = card(title=obj.name, body=desc)
        content = obj_card + query_nearby(obj) + query_latest()
    except Kaomoji.DoesNotExist:
        raise Http404("Kaomoji does not exist")
    return render(request, 'bsbay_base.html', {'title': title, 'content': content, 'sidebar':default_sidebar()})