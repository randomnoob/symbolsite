from django.urls import path
from django.views.generic import TemplateView


from .content import PRIVACY_POLICY, TRADEMARK

domain = "https://symbolspace.net/"
site_name = "SymbolSpace"
PRIVACY_POLICY = PRIVACY_POLICY.replace("LinuxPip", site_name)
PRIVACY_POLICY = PRIVACY_POLICY.replace("https://linuxpip.org/", domain)


urlpatterns = [
    path("privacy-policy/", TemplateView.as_view(template_name="bsbay_flatpages.html",\
                                            extra_context={
                                                'title':"Privacy Policy",
                                                'content':PRIVACY_POLICY,
                                            }), name="privacy_policy"),
    path("trademark/", TemplateView.as_view(template_name="bsbay_flatpages.html",\
                                            extra_context={
                                                'title':"Trademark & Licensing",
                                                'content':TRADEMARK,
                                            }), name="trademark"),
    path("cookie-policy/", TemplateView.as_view(template_name="bsbay_flatpages.html",\
                                            extra_context={
                                                'title':"Cookie Policy",
                                                'content':"",
                                            }), name="cookie_policy"),
    path("contact/", TemplateView.as_view(template_name="bsbay_flatpages.html",\
                                            extra_context={
                                                'title':"Contact us",
                                                'content':"",
                                            }), name="contact")
]
