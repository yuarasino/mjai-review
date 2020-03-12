from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("vue.urls", "vue"))),
    path("api/", include(("api.urls", "api"))),
]
