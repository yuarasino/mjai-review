from django.urls import path

from .views import pages

urlpatterns = [path("", pages.IndexPage.as_view(), name="index")]
