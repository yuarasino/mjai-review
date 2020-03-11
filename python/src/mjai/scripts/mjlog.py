import subprocess
from typing import Tuple
from urllib.parse import urlparse, parse_qsl

from .. import consts


def fetch_mjlog_xml(mjlog_id: str) -> bytes:
    """天鳳の牌譜IDから、mjlog形式のxmlをダウンロードする
    >>> from mjai.scripts.mjlog import fetch_mjlog_xml
    >>> mjlog_id = "2011020613gm-00a9-0000-3774f8d1"
    >>> xml = fetch_mjlog_xml(mjlog_id)
    """
    fetch_url = consts.MJLOG_FETCH_URL.format(mjlog_id=mjlog_id)
    result = subprocess.run(
        ["curl", "-SsL", "--compressed", f"{fetch_url}"],
        capture_output=True,
        check=True
    )
    return result.stdout

def get_mjlog_id_and_target_wind(url: str) -> Tuple[str, int]:
    """天鳳の牌譜URLから、mjlog_idと視点を取得する
    >>> from mjai.scripts.mjlog import get_mjlog_id_and_target_wind
    >>> url = "http://tenhou.net/0/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
    >>> mjlog_id, target_wind = get_mjlog_id_and_target_wind(url)
    """
    query = urlparse(url).query
    query_dict = dict(parse_qsl(query))
    mjlog_id = query_dict["log"]
    target_wind = int(query_dict.get("tw", '0'))
    return mjlog_id, target_wind
