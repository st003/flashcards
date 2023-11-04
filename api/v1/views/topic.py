from rest_framework import generics

from api.v1.serializers import TopicSerializer
from words.models import Topic


class TopicsV1ApiView(generics.ListAPIView):
    """Read-only endpoint for querying all Topics."""
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
