from rest_framework import generics

from api.v1.serializers import WordSerializer
from words.models import Word


class WordV1ApiView(generics.RetrieveAPIView):
    """Read-only endpoint for querying a single Word."""
    queryset = Word.objects.all()
    serializer_class = WordSerializer
