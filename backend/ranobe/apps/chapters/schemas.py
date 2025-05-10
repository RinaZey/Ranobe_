from rest_framework import serializers

class ChapterSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    number = serializers.IntegerField()
    text = serializers.CharField()

class ChapterCreateSerializer(ChapterSerializer):
    ranobe = None

class ChapterFilterSerializer(serializers.Serializer):
    ranobe = serializers.IntegerField(min_value=1, required=False)
    order_by = serializers.CharField(required=False)

class ChapterUpdateSerializer(ChapterSerializer):
    title = serializers.CharField(required=False)
    ranobe = serializers.IntegerField(required=False)
    text = serializers.CharField(required=False)

class ChapterShortenedSerializer(ChapterSerializer):
    text = None
