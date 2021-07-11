import random
from collections import deque

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Word


# VIEWS
@require_http_methods(['GET'])
def index(request):
    """Renders start page."""
    return render(request, 'words/index.html')


@require_http_methods(['GET'])
def flashcard(request):
    """Renders the flash card page."""
    return render(request, 'words/flashcard.html')


@require_http_methods(['GET'])
def get_word(request):
    """Returns a random word in JSON."""

    filters = {}
    if request.GET.get('category'):
        filters['category'] = request.GET['category']
    if request.GET.get('topic'):
        filters['topics__name'] = request.GET['topic']

    words = Word.objects.filter(**filters).all()
    word_count = len(words)

    if word_count > 0:

        # when filtering, you should purge the history
        if request.GET.get('purgeMem') == 'true':
            new_max_len = (word_count - 1) if word_count < settings.CONFIG_HISTORY_MEM else settings.CONFIG_HISTORY_MEM
            settings.WORD_ID_MEM = deque(maxlen=new_max_len)

        rand_index = 0
        selected_word_id = 0
        word = None

        # ending random selection after making the same number of selections
        # as the maxlen will prevent an infinite loop when the word_count is
        # less than or equal to the maxlen.
        #
        # TODO - Ideally, maxlen should be auto-set on startup to catch situations
        # when the total word count is small that the CONFIG_HISTORY_MEM
        for i in range(settings.WORD_ID_MEM.maxlen):
            rand_index = random.randrange(0, word_count -1) if word_count > 1 else 0
            selected_word_id = words[rand_index].pk

            if selected_word_id not in settings.WORD_ID_MEM:
                word = words[rand_index]
                break

        else:
            word = words[rand_index]

        settings.WORD_ID_MEM.append(selected_word_id)

        return JsonResponse({'count': word_count ,'en': word.en, 'jp': word.jp})

    else:
        return JsonResponse({'message': 'There were no results returned'}, status=404)
