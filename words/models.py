from django.db import models


class Word(models.Model):
    """Model defining a word and it's translation."""

    NOUN = 1
    VERB = 2
    ADJ = 3
    CATEGORIES = [
        (NOUN, 'Noun'),
        (VERB, 'Verb'),
        (ADJ, 'Adjective')
    ]

    en = models.CharField(max_length=64)
    jp = models.CharField(max_length=64)
    category = models.IntegerField(null=True, blank=True, choices=CATEGORIES)

    def __str__(self):
        return self.en
    
    def __repr__(self):
        return f'Word(en={self.en})'
