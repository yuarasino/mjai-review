import pytest

from review.models import Review


class TestReviewCreateSerializer:
    @pytest.fixture
    def target_serializer(self):
        from review.serializers import ReviewCreateSerializer

        return ReviewCreateSerializer

    @pytest.mark.django_db
    def test_valid_review_create_serializer(self, target_serializer):
        post_data = {
            "mjlog_view_url": "https://tenhou.net/0/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
        }
        serializer = target_serializer(data=post_data)
        assert serializer.is_valid()
        assert serializer.create(serializer.validated_data)

    def test_invalid_review_create_serializer(self, target_serializer):
        post_data = {
            "mjlog_view_url": "https://example.com/0/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
        }
        serializer = target_serializer(data=post_data)
        assert not serializer.is_valid()


class TestReviewListSerializer:
    @pytest.fixture
    def target_serializer(self):
        from review.serializers import ReviewListSerializer

        return ReviewListSerializer

    @pytest.mark.django_db
    def test_review_list_serializer(self, target_serializer):
        reviews = [
            Review(mjlog_id="2011020613gm-00a9-0000-3774f8d1", target_actor=2),
            Review(mjlog_id="2011020417gm-00a9-0000-b67fcaa3", target_actor=1),
        ]
        serializer = target_serializer(reviews, many=True)
        data = serializer.data
        assert len(data) == 2
        assert (
            data[0]["mjlog_view_url"]
            == "https://tenhou.net/0/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
        )
        assert data[0]["status"] == "予約中"
