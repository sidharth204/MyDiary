from django.contrib import admin

from .models import DiaryEntry


@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'user',
        'category',
        'mood',
        'is_pinned',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'category',
        'mood',
        'is_pinned',
        'created_at',
    )

    search_fields = (
        'title',
        'content',
        'user__username',
    )

    ordering = (
        '-created_at',
    )