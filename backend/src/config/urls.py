from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("frontend.urls", "frontend"))),
    path("", include(("review.urls", "review"))),
]
