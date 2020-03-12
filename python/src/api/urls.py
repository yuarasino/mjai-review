from django.urls import path

from review import views as review_views

urlpatterns = [
    path("review/create", review_views.ReviewCreateAPI.as_view(), name="review_create")
]
