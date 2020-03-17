from django.urls import path

from . import views

urlpatterns = [
    path("api/review/create", views.ReviewCreateAPIView.as_view(), name="review_create"),
]
