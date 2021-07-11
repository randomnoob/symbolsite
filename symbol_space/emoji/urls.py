from django.urls import path
from django.shortcuts import redirect
from django.views.generic import TemplateView


from .views import EmojiTerraDetail, CategoryView, UnicodeVersionView

urlpatterns = [
    path("", TemplateView.as_view(template_name="bsbay_home.html"), name="bsbay_home"),
    path("<slug:slug>/", EmojiTerraDetail.as_view(), name="emoji_detail_slug"),
    path("categories", CategoryView.as_view(), name="all_category"),
    path("versions", UnicodeVersionView.as_view(), name="all_versions")
]
