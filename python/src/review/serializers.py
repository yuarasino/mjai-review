from rest_framework import serializers

from mjai.mjlog import get_mjlog_id_and_target_wind

from .models import Review


class ReviewListSerializer(serializers.ModelSerializer):
    mjlog_watch_url = serializers.URLField()

    class Meta:
        model = Review
        fields = ["id", "mjlog_watch_url", "review_status", "reserved_at"]


class ReviewCreateSerializer(serializers.Serializer):
    mjlog_watch_url = serializers.URLField()

    def create(self, validated_data) -> Review:
        mjlog_id, target_wind = get_mjlog_id_and_target_wind(validated_data["mjlog_watch_url"])
        return Review.objects.create(
            mjlog_id=mjlog_id, 
            target_wind=target_wind
        )
