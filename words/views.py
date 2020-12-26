import random
from collections import deque

from django.http import JsonResponse
from django.shortcuts import render

from .models import Word


LAST_IDS = deque(maxlen=5)


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

    rand_id = 0
    while True:
        rand_id = random.randrange(1, WORD_COUNT + 1)
        if rand_id not in LAST_IDS:
            break
    LAST_IDS.append(rand_id)

    # get word
    w = Word.objects.get(pk=rand_id)
    return JsonResponse({'en': w.en, 'jp': w.jp})
