from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from mjai.urls import get_mjlog_file_url, get_mjlog_view_url


class Review(models.Model):
    class Meta:
        db_table = "review"
        verbose_name = verbose_name_plural = _("レビュー")

    class Status(models.IntegerChoices):
        Reserved = 1, "予約中"
        Started = 2, "レビュー中"
        Ended = 3, "レビュー完了"
        Error = 4, "エラー終了"

    mjlog_id = models.CharField(_("牌譜ID"), max_length=63)
    target_actor = models.PositiveSmallIntegerField(_("視点"))
    status = models.PositiveSmallIntegerField(
        _("レビュー状況"), choices=Status.choices, default=Status.Reserved
    )
    result_json = models.TextField(_("結果JSON"), blank=True)
    reserved_at = models.DateTimeField(_("予約時刻"), default=timezone.now)
    started_at = models.DateTimeField(_("レビュー開始時刻"), blank=True, null=True)
    ended_at = models.DateTimeField(_("レビュー完了時刻"), blank=True, null=True)

    @property
    def mjlog_view_url(self) -> str:
        return get_mjlog_file_url(self.mjlog_id, self.target_actor)

    @property
    def mjlog_file_url(self) -> str:
        return get_mjlog_file_url(self.mjlog_id)
