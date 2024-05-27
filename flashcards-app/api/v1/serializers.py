from rest_framework import serializers

from words.models import Topic


class CategorySerializer(serializers.Serializer):
    # TODO - check options for these serializer functions
    name = serializers.CharField()
    value = serializers.IntegerField()


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
