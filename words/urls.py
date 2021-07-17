from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('flashcard/', views.flashcard, name="flashcard"),
    path('get_category/', views.get_category, name="get_category"),
    path('get_topic/', views.get_topic, name="get_topic"),
    path('get_word/', views.get_word, name="get_word")
]
