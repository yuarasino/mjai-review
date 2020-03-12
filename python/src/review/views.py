from rest_framework.generics import CreateAPIView

from .serializers import ReviewCreateSerializer


class ReviewCreateAPI(CreateAPIView):
    serializer_class = ReviewCreateSerializer
