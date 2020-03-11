import subprocess

from .. import consts


def fetch_mjlog_xml(mjlog_id: str) -> bytes:
    """天鳳の牌譜IDから、mjlog形式のxmlをダウンロードする
    >>> from mjai.scripts.mjlog import fetch_mjlog_xml
    >>> fetch_mjlog_xml("2011020613gm-00a9-0000-3774f8d1")
    """
    fetch_url = consts.MJLOG_FETCH_URL.format(mjlog_id=mjlog_id)
    result = subprocess.run(
        ["curl", "-SsL", "--compressed", f"{fetch_url}"],
        capture_output=True,
    )
    return result.stdout
