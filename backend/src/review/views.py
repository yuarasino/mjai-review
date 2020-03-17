from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Review
from .serializers import ReviewCreateSerializer, ReviewListSerializer


class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewCreateSerializer


class ReviewListAPIView(ListAPIView):
    serializer_class = ReviewListSerializer
    queryset = Review.objects.all().order_by("-reserved_at")
