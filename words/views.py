import random

from django.http import JsonResponse
from django.shortcuts import render

from .models import Word


# VIEWS
def index(request):
    """Renders start page."""
    return render(request, 'words/index.html')

def flashcard(request):
    """Renders the flash card page."""
    return render(request, 'words/flashcard.html')

def get_word(request):
    """Returns a random word in JSON."""
    WORD_COUNT = Word.objects.count()
    
    last_id = request.GET.get('id', 0)
    rand_id = 0
    while True:
        rand_id = random.randrange(1, WORD_COUNT + 1)
        if rand_id != int(last_id):
            break

    # get word
    w = Word.objects.get(pk=rand_id)
    return JsonResponse({'id': w.id, 'en': w.en, 'jp': w.jp})
