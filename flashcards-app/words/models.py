from django.db import models


class Topic(models.Model):
    """Topic for grouping words."""

    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Topic(name={self.name})'


class Word(models.Model):
    """A word, its translation, and category."""

    NOUN = 1
    VERB = 2
    ADJ = 3
    ADVERB = 4
    PHRASE = 5
    COUNTER = 6

    CATEGORIES = [
        (NOUN, 'Noun'),
        (VERB, 'Verb'),
        (ADJ, 'Adjective'),
        (ADVERB, 'Adverb'),
        (PHRASE, 'Phrase'),
        (COUNTER, 'Counter')
    ]

    en = models.CharField(max_length=64)
    jp = models.CharField(max_length=64)
    category = models.IntegerField(blank=True, null=True, db_index=True, choices=CATEGORIES)
    topics = models.ManyToManyField(Topic, blank=True, related_name="words")

    def __str__(self):
        return self.en

    def __repr__(self):
        return f'Word(en={self.en})'
