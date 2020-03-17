from django.core.validators import RegexValidator, _lazy_re_compile
from django.utils.translation import gettext_lazy as _

from . import consts

mjlog_view_url_validator = RegexValidator(
    _lazy_re_compile(consts.MJLOG_VIEW_URL_REGEX), message=_("有効な牌譜閲覧URLではありません。"), code="invalid",
)
