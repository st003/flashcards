from django.contrib import admin

from .models import Word, Topic


class TopicInline(admin.TabularInline):
    model = Word.topics.through


class TopicAdmin(admin.ModelAdmin):
    """Custom ModelAdmin for Topic model."""

    # table configs
    list_display = ('name',)
    list_per_page = 25
    search_fields = ['name']

    inlines = [TopicInline]


class WordAdmin(admin.ModelAdmin):
    """Custom ModelAdmin for Word model."""

    # table configs
    list_display = ('en', 'jp', 'category')
    list_per_page = 25
    list_filter = ('category',)
    search_fields = ['en']

    # add/edit form configs
    filter_horizontal = ('topics',)


# Register your models here.
admin.site.register(Topic, TopicAdmin)
admin.site.register(Word, WordAdmin)
