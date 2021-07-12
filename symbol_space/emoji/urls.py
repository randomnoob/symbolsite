from django.urls import path
from django.shortcuts import redirect
from django.views.generic import TemplateView


from .views import EmojiTerraDetail, CategoryView, CategoryListView

urlpatterns = [
    path("", TemplateView.as_view(template_name="bsbay_home.html"), name="bsbay_home"),
    path("categories/", CategoryListView.as_view(), name="category_all"),
    path("c/<slug:slug>/", CategoryView.as_view(), name="category_detail"),
    # path("versions", UnicodeVersionView.as_view(), name="all_versions"),
    path("<slug:slug>/", EmojiTerraDetail.as_view(), name="emoji_detail"),
]
