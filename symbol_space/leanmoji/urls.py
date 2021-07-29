from django.urls import path
from django.shortcuts import redirect
from django.views.generic import TemplateView

from .views import detail, homeview, cateview, KaomojiListView
# from .views import EmojiTerraDetail, CategoryView, CategoryListView, HomeView

urlpatterns = [
    path("home", homeview, name="emo_homeview"),
    path("all", KaomojiListView.as_view(), name="emo_allview"),
    path("c/<str:category>", cateview, name="emo_category"),
    path("<slug:slug>", detail, name="emo_detail"),
    # path("c/<slug:slug>/", CategoryView.as_view(), name="category_detail"),
    # # path("versions", UnicodeVersionView.as_view(), name="all_versions"),
    # path("<slug:slug>/", EmojiTerraDetail.as_view(), name="emoji_detail"),
]
