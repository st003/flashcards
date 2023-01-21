from django.urls import path

from .views.topic import TopicsV1ApiView
from .views.word import WordV1ApiView

urlpatterns = [
    path('topic/', TopicsV1ApiView.as_view()),
    path('word/<int:pk>/', WordV1ApiView.as_view())
]
