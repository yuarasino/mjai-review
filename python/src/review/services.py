import json
import subprocess
from logging import getLogger
from pathlib import Path
from typing import Any, Dict, List, TextIO

from django.db.models import QuerySet
from django.utils import timezone

from mjai import mjlog

from .models import Review

logger = getLogger("project")


class ReviewError(Exception):
    pass


class ReviewService:
    @classmethod
    def get_queryset(cls) -> QuerySet:
        return Review.objects.all().order_by("-reserved_at")

    def run(self, review: Review):
        review.review_status = Review.Status.Started
        review.started_at = timezone.now()
        review.save()
        try:
            review_result = self.do_review(review)
            review.review_result = review_result
            review.review_status = Review.Status.Ended
        except Exception as e:
            logger.exception(e)
            review.review_result = str(e)
            review.review_status = Review.Status.Error
        review.ended_at = timezone.now()
        review.save()

    def do_review(self, review: Review) -> str:
        results = []
        with mjlog.get_mjson_file(review.mjlog_id) as mjson_file:
            with mjson_file.open() as f:
                mjson = json.loads(f"[{','.join(row for row in f if row)}]")
            for i, action in enumerate(mjson):
                if action["type"] == "tsumo" and action["actor"] == review.target_wind:
                    evaluation = self.get_evaluation(mjson_file, review.target_wind, i)
                    results.append(evaluation)
                if i > 20:
                    break
        return json.dumps(results)

    def get_evaluation(self, mjson_file: Path, target_wind: int, i: int) -> List[Dict[str, Any]]:
        result = subprocess.run(
            ["./system.exe", "mjai_log", mjson_file, str(target_wind), str(i)],
            cwd="/opt/akochan",
            capture_output=True,
            check=True,
        )
        return json.loads(result.stdout.strip().split(b"\n")[-1])
