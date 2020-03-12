from logging import getLogger

from mjai import mjlog

from .models import Review


class ReviewService:
    def run(review: Review):
        mjson_text = mjlog.get_mjson_text()
        assert(mjson_text)
