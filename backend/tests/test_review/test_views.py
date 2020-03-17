import pytest
from django.urls import reverse
from rest_framework.test import APIRequestFactory


class TestReviewCreateView:
    @pytest.fixture
    def target_view(self):
        from review.views import ReviewCreateAPIView

        return ReviewCreateAPIView.as_view()

    @pytest.fixture
    def target_url(self):
        return reverse("review:review_create")

    @pytest.mark.django_db
    def test_valid_review_create_serializer(self, rf, target_view, target_url):
        post_data = {
            "mjlog_view_url": "https://tenhou.net/0/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
        }
        request = rf.post(target_url, post_data)
        response = target_view(request)
        assert response.status_code == 201

    def test_invalid_review_create_serializer(self, rf, target_view, target_url):
        post_data = {
            "mjlog_view_url": "https://example.com/0/?log=2011020613gm-00a9-0000-3774f8d1&tw=2"
        }
        request = rf.post(target_url, post_data)
        response = target_view(request)
        assert response.status_code == 400
