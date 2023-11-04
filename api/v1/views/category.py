from rest_framework import generics

from api.v1.serializers import CategorySerializer
from words.models import Word


class CategoriesV1ApiView(generics.ListAPIView):
    """Read-only endpoint for querying all Categories."""
    serializer_class = CategorySerializer

    # categories are not currently defined database-side so we need to
    # grab them from the Word model
    def get_queryset(self):
        return [{'name': name, 'value': value} for value, name in Word.CATEGORIES]
