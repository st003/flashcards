from django.contrib import admin

from .models import Word


class WordAdmin(admin.ModelAdmin):
    """Custom ModelAdmin for Word model."""
    list_display = ('en', 'jp', 'category')
    list_per_page = 25
    list_filter = ('category',)
    search_fields = ['en']


# Register your models here.
admin.site.register(Word, WordAdmin)
