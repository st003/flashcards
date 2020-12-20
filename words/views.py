from django.shortcuts import render


def index(request):
    return render(request, 'words/index.html')

def flashcard(request):
    return render(request, 'words/flashcard.html')
