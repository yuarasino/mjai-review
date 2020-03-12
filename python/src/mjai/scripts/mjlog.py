import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Dict, Tuple
from urllib.parse import parse_qsl, urlparse
from uuid import uuid4

from .. import consts


def get_mjlog_id_and_target_wind(url: str) -> Tuple[str, int]:
    """天鳳の牌譜URLから、mjlog_idと視点を取得する
    >>> from mjai.scripts.mjlog import get_mjlog_id_and_target_wind
    >>> url = "http://tenhou.net/3/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
    >>> mjlog_id, target_wind = get_mjlog_id_and_target_wind(url)
    """
    query = urlparse(url).query
    query_dict = dict(parse_qsl(query))
    mjlog_id = query_dict["log"]
    target_wind = int(query_dict.get("tw", "0"))
    return mjlog_id, target_wind


def fetch_mjlog(mjlog_id: str) -> bytes:
    """天鳳の牌譜IDから、mjlog形式のgzipをダウンロードする
    >>> from mjai.scripts.mjlog import fetch_mjlog
    >>> mjlog_id = "2011020613gm-00a9-0000-3774f8d1"
    >>> mjlog = fetch_mjlog(mjlog_id)
    """
    fetch_url = consts.MJLOG_FETCH_URL.format(mjlog_id=mjlog_id)
    result = subprocess.run(
        ["curl", "-SsL", "--compressed", "--raw", f"{fetch_url}"], capture_output=True, check=True
    )
    return result.stdout


def convert_mjlog(mjlog: bytes) -> str:
    """mjlog(gzip)をmjson形式のjsonに変換する
    >>> from mjai.scripts.mjlog import convert_mjlog
    >>> mjlog = <fetch_mjlogで取得したデータ>
    >>> mjson = convert_mjlog(mjlog)
    """
    with TemporaryDirectory() as tmp_dirname:
        tmp_fileName = str(uuid4())
        mjlog_path = Path(tmp_dirname) / f"{tmp_fileName}.mjlog"
        mjson_path = Path(tmp_dirname) / f"{tmp_fileName}.mjson"
        with mjlog_path.open("wb") as f:
            f.write(mjlog)
        subprocess.run(
            ["mjai", "convert", f"{mjlog_path.absolute()}", f"{mjson_path.absolute()}"], check=True
        )
        with mjson_path.open("r") as f:
            mjson = f.read()
    return mjson
