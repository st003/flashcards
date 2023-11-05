import random
from collections import deque

from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from words.models import Word


class WordRandV1ApiView(APIView):

    def get(self, request):
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
            # when the total word count is smaller that the CONFIG_HISTORY_MEM
            for i in range(settings.WORD_ID_MEM.maxlen):
                rand_index = random.randint(0, word_count -1) if word_count > 1 else 0
                selected_word_id = words[rand_index].pk

                if selected_word_id not in settings.WORD_ID_MEM:
                    word = words[rand_index]
                    break

            else:
                word = words[rand_index]

            settings.WORD_ID_MEM.append(selected_word_id)

            return Response({'count': word_count ,'en': word.en, 'jp': word.jp})

        else:
            return Response({'message': 'There were no results returned'}, status=status.HTTP_404_NOT_FOUND)
