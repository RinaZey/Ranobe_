from django.forms import CharField
from rest_framework import serializers
from backend.apps.chapters.schemas import ChapterShortenedSerializer
from backend.apps.metadata.schemas import (
    TagSerializer,
    GenreSerializer
)

from ranobes.models import Ranobe

class RanobeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    slug = serializers.SlugField(required=False)

    cover = serializers.ImageField(required=False)

    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    title = serializers.CharField()
    creator = CharField()

    status = serializers.ChoiceField(Ranobe.STATUS)

    chapters = ChapterShortenedSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True)
    genres = GenreSerializer(many=True)

class RanobeFilterSerializer(serializers.Serializer):
    tags = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False
    )
    genres = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False
    )
    order_by = serializers.CharField(required=False)

class RanobeCreateSerializer(RanobeSerializer):
    creator = serializers.CharField(required=False)
    tags = serializers.ListField(
        child=serializers.IntegerField(min_value=1)
    )
    genres = serializers.ListField(
        child=serializers.IntegerField(min_value=1)
    )

class RanobeUpdateSerializer(RanobeSerializer):
    title = serializers.CharField(required=False)
    tags = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False
    )
    genres = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False
    )

class RanobeListSerializer(RanobeSerializer):
    chapters = None
    updated_at = None

class RanobeShortenedSerializer(RanobeSerializer):
    id = None
    chapters = None
    updated_at = None
    created_at = None
    tags = None
    genres = None
