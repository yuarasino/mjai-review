import pytest
from django.core.exceptions import ValidationError


class TestMjlogViewUrlValidators:
    @pytest.fixture
    def target_func(self):
        from mjai.validators import mjlog_view_url_validator

        return mjlog_view_url_validator

    def test_valid_mjlog_view_url_validator(self, target_func):
        valid_mjlog_view_url = "https://tenhou.net/3/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
        target_func(valid_mjlog_view_url)

    def test_invalid_mjlog_view_url_validator(self, target_func):
        invalid_mjlog_view_url = "https://example.com/3/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
        with pytest.raises(ValidationError):
            target_func(invalid_mjlog_view_url)
