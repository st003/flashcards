from django.contrib import admin

from .models import Word


class WordAdmin(admin.ModelAdmin):
    """Custom ModelAdmin for Word model."""
    list_display = ('en', 'jp', 'category')


# Register your models here.
admin.site.register(Word, WordAdmin)
