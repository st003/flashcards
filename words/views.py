from django.shortcuts import render
from django.views.decorators.http import require_http_methods


# VIEWS
@require_http_methods(['GET'])
def index(request):
    """Renders start page."""
    return render(request, 'words/index.html')


@require_http_methods(['GET'])
def flashcard(request):
    """Renders the flash card page."""
    return render(request, 'words/flashcard.html')
