import json
import random
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.shortcuts import render

class CategoryListView(ListView):
    model= Category
    template_name= 'bsbay_category_all.html'
