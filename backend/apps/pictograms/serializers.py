from rest_framework import serializers

from .models import Pictogram


class PictogramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictogram
        fields = [
            "id",
            "arasaac_id",
            "keyword",
            "description",
            "image_url",
            "created_at",
            "updated_at",
        ]
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
