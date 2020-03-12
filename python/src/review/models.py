from django.db import models
from django.utils import timezone


class Review(models.Model):
    class Meta:
        db_table = "reviews"
        verbose_name = verbose_name_plural = "レビュー"

    class Status(models.IntegerChoices):
        Reserved = 1, "予約中"
        Started = 2, "レビュー中"
        Ended = 3, "レビュー完了"

    mjlog_id = models.CharField("牌譜ID", max_length=63)
    target_wind = models.PositiveSmallIntegerField("視点", default=0)
    review_status = models.PositiveSmallIntegerField(
        "レビューの状況", choices=Status.choices, default=Status.Reserved
    )
    review_json = models.TextField("レビューのJSON", blank=True)
    reserved_at = models.DateTimeField("予約時刻", default=timezone.now)
    started_at = models.DateTimeField("開始時刻", null=True, blank=True)
    ended_at = models.DateTimeField("終了時刻", null=True, blank=True)
