from rest_framework import serializers

from words.models import Topic, Word


class CategorySerializer(serializers.Serializer):
    # TODO - check options for these serializer functions
    name = serializers.CharField()
    value = serializers.IntegerField()


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

