import pytest


class TestReviewCreateSerializer:
    @pytest.fixture
    def target_serializer(self):
        from review.serializers import ReviewCreateSerializer

        return ReviewCreateSerializer

    @pytest.mark.django_db
    def test_valid_review_create_serializer(self, target_serializer):
        post_data = {
            "mjlog_view_url": "https://tenhou.net/3/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
        }
        serializer = target_serializer(data=post_data)
        assert serializer.is_valid()
        assert serializer.create(serializer.validated_data)

    def test_invalid_review_create_serializer(self, target_serializer):
        post_data = {
            "mjlog_view_url": "https://example.com/3/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
        }
        serializer = target_serializer(data=post_data)
        assert not serializer.is_valid()
