from django.urls import path

from .views.category import CategoriesV1ApiView
from .views.topic import TopicsV1ApiView
from .views.word import WordV1ApiView


urlpatterns = [
    path('category/', CategoriesV1ApiView.as_view(), name='category'),
    path('topic/', TopicsV1ApiView.as_view(), name='topic'),
    path('word/<int:pk>/', WordV1ApiView.as_view())
]
