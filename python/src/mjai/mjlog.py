import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Dict, Tuple
from urllib.parse import parse_qsl, urlparse

from . import consts


def get_mjlog_id_and_target_wind(mjlog_watch_url: str) -> Tuple[str, int]:
    """天鳳の観戦URLから、天鳳牌譜IDと視点を取得する
    >>> from mjai.mjlog import get_mjlog_id_and_target_wind
    >>> mjlog_watch_url = "http://tenhou.net/3/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
    >>> get_mjlog_id_and_target_wind(mjlog_watch_url)
    ("2011020613gm-00a9-0000-3774f8d1", 2)
    """
    query = urlparse(mjlog_watch_url).query
    query_dict = dict(parse_qsl(query))
    mjlog_id = query_dict["log"]
    target_wind = int(query_dict.get("tw", "0"))
    return mjlog_id, target_wind


def get_mjlog_fetch_url(mjlog_id: str) -> str:
    """天鳳牌譜IDから、天鳳牌譜URLを取得する
    >>> from mjai.mjlog import get_mjlog_fetch_url
    >>> mjlog_id = "2011020613gm-00a9-0000-3774f8d1"
    >>> get_mjlog_fetch_url(mjlog_id)
    "http://tenhou.net/0/log/?2011020613gm-00a9-0000-3774f8d1"
    """
    return consts.MJLOG_FETCH_URL.format(mjlog_id=mjlog_id)


def get_mjlog_watch_url(mjlog_id: str, target_wind: int) -> str:
    """天鳳牌譜IDから、天鳳牌譜URLを取得する
    >>> from mjai.mjlog import get_mjlog_fetch_url
    >>> mjlog_id, target_wind = "2011020613gm-00a9-0000-3774f8d1", 2
    >>> get_mjlog_fetch_url(mjlog_id, target_wind)
    "http://tenhou.net/3/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
    """
    return consts.MJLOG_WATCH_URL.format(mjlog_id=mjlog_id, target_wind=target_wind)


def get_mjson_text(mjlog_id: str) -> str:
    """牌譜IDからmjson形式のtextに変換する
    >>> from mjai.mjlog import get_mjson_text
    >>> mjlog_id = "2011020613gm-00a9-0000-3774f8d1"
    >>> get_mjson_text(mjlog_id)
    "<mjson形式のtext>"
    """
    mjlog_gzip = fetch_mjlog_gzip(mjlog_id)
    with TemporaryDirectory() as tmp_dir:
        mjlog_tmp_path = Path(tmp_dir) / f"{mjlog_id}.mjlog"
        mjson_tmp_path = Path(tmp_dir) / f"{mjlog_id}.mjson"
        with mjlog_tmp_path.open("wb") as f:
            f.write(mjlog_gzip)
        subprocess.run(
            ["mjai", "convert", f"{mjlog_tmp_path.absolute()}", f"{mjson_tmp_path.absolute()}"],
            check=True,
        )
        with mjson_tmp_path.open("r") as f:
            mjson_text = f.read()
    return mjson_text


def fetch_mjlog_gzip(mjlog_id: str) -> bytes:
    """天鳳の牌譜URLから、mjlog形式のgzipをダウンロードする
    >>> from mjai.mjlog import fetch_mjlog_gzip
    >>> mjlog_id = "2011020613gm-00a9-0000-3774f8d1"
    >>> fetch_mjlog_gzip(mjlog_id)
    b"<mjlog形式のgzip>"
    """
    fetch_url = consts.MJLOG_FETCH_URL.format(mjlog_id=mjlog_id)
    result = subprocess.run(
        ["curl", "-SsL", "--compressed", "--raw", f"{fetch_url}"], capture_output=True, check=True
    )
    return result.stdout
