from rest_framework.generics import CreateAPIView

from .serializers import ReviewCreateSerializer


class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewCreateSerializer
