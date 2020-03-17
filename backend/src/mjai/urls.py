from typing import Tuple
from urllib.parse import parse_qsl, urlparse

from . import consts


def parse_mjlog_view_url(mjlog_view_url: str) -> Tuple[str, int]:
    """牌譜閲覧URLから、牌譜IDと視点を取得する"""
    query = urlparse(mjlog_view_url).query
    query_dict = dict(parse_qsl(query))
    mjlog_id = query_dict["log"]
    target_actor = int(query_dict.get("tw", "0"))
    return mjlog_id, target_actor


def get_mjlog_view_url(mjlog_id: int, target_actor: int) -> str:
    """牌譜IDと視点から牌譜閲覧URLを取得する"""
    return consts.MJLOG_VIEW_URL_PLACEHOLDER.format(mjlog_id=mjlog_id, target_actor=target_actor)


def get_mjlog_file_url(mjlog_id: int) -> str:
    """牌譜IDから牌譜ファイルURLを取得する"""
    return consts.MJLOG_FILE_URL_PLACEHOLDER.format(mjlog_id=mjlog_id)
