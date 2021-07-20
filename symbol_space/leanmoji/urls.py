from django.urls import path
from django.shortcuts import redirect
from django.views.generic import TemplateView

from .views import detail
# from .views import EmojiTerraDetail, CategoryView, CategoryListView, HomeView

urlpatterns = [
    path("<slug:slug>", detail, name="emo_view"),
    # path("categories/", CategoryListView.as_view(), name="category_all"),
    # path("c/<slug:slug>/", CategoryView.as_view(), name="category_detail"),
    # # path("versions", UnicodeVersionView.as_view(), name="all_versions"),
    # path("<slug:slug>/", EmojiTerraDetail.as_view(), name="emoji_detail"),
]
