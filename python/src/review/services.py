from logging import getLogger

from django.db.models import QuerySet
from mjai import mjlog

from .models import Review


class ReviewService:
    @classmethod
    def get_queryset(cls) -> QuerySet:
        return Review.objects.all().order_by("-reserved_at")

    def run(self, review: Review):
        mjson_text = mjlog.get_mjson_text(review.mjlog_id)
        assert(mjson_text)
