from rest_framework import serializers

from mjai.urls import parse_mjlog_view_url
from mjai.validators import mjlog_view_url_validator

from .models import Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["mjlog_view_url"]

    mjlog_view_url = serializers.URLField(validators=[mjlog_view_url_validator])

    def create(self, validated_data):
        mjlog_view_url = validated_data.pop("mjlog_view_url")
        mjlog_id, target_actor = parse_mjlog_view_url(mjlog_view_url)
        validated_data["mjlog_id"] = mjlog_id
        validated_data["target_actor"] = target_actor
        return super().create(validated_data)


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "status", "mjlog_view_url", "reserved_at"]

    status = serializers.CharField(source="get_status_display")
    reserved_at = serializers.DateTimeField(format=r"%Y-%m-%d %H:%M")
