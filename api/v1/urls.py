from django.urls import path

from .views.category import CategoriesV1ApiView
from .views.topic import TopicsV1ApiView
from .views.word import WordRandV1ApiView


urlpatterns = [
    path('category/', CategoriesV1ApiView.as_view(), name='category'),
    path('topic/', TopicsV1ApiView.as_view(), name='topic'),
    path('word/rand/', WordRandV1ApiView.as_view(), name='word_rand')
]
