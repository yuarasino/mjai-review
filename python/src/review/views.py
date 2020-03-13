from rest_framework.generics import CreateAPIView, ListAPIView

from mjai import mjlog

from .serializers import ReviewCreateSerializer, ReviewListSerializer
from .services import ReviewService


class ReviewListAPI(ListAPIView):
    serializer_class = ReviewListSerializer
    queryset = ReviewService.get_queryset()


class ReviewCreateAPI(CreateAPIView):
    serializer_class = ReviewCreateSerializer

    def perform_create(self, serializer: ReviewCreateSerializer):
        review = serializer.save()
        service = ReviewService()
        service.run(review)
