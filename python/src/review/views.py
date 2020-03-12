from rest_framework.generics import CreateAPIView

from mjai import mjlog

from .serializers import ReviewCreateSerializer
from .services import ReviewService


class ReviewCreateAPI(CreateAPIView):
    serializer_class = ReviewCreateSerializer

    def perform_create(self, serializer: ReviewCreateSerializer):
        review = serializer.save()
        service = ReviewService()
        service.run(review)
