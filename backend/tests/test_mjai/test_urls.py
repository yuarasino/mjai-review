import pytest


class TestParseMjlogViewUrl:
    @pytest.fixture
    def target_func(self):
        from mjai.urls import parse_mjlog_view_url

        return parse_mjlog_view_url

    @pytest.mark.parametrize(
        "mjlog_view_url, expected",
        [
            (
                "https://tenhou.net/3/?log=2011020613gm-00a9-0000-3774f8d1&tw=2",
                ("2011020613gm-00a9-0000-3774f8d1", 2),
            ),
            (
                "https://tenhou.net/3/?log=2011020613gm-00a9-0000-3774f8d1",
                ("2011020613gm-00a9-0000-3774f8d1", 0),
            ),
        ],
    )
    def test_parse_mjlog_view_url(self, target_func, mjlog_view_url, expected):
        actual = target_func(mjlog_view_url)

        assert actual == expected


class TestGetMjlogViewUrl:
    @pytest.fixture
    def target_func(self):
        from mjai.urls import get_mjlog_view_url

        return get_mjlog_view_url

    def test_get_mjlog_view_url(self, target_func):
        expected = "https://tenhou.net/3/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"

        mjlog_id = "2011020613gm-00a9-0000-3774f8d1"
        target_actor = 2
        actual = target_func(mjlog_id, target_actor)

        assert actual == expected


class TestGetMjlogFileUrl:
    @pytest.fixture
    def target_func(self):
        from mjai.urls import get_mjlog_file_url

        return get_mjlog_file_url

    def test_get_mjlog_file_url(self, target_func):
        expected = "https://tenhou.net/0/log/?2011020613gm-00a9-0000-3774f8d1"

        mjlog_id = "2011020613gm-00a9-0000-3774f8d1"
        actual = target_func(mjlog_id)

        assert actual == expected
