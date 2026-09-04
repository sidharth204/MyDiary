from django.db import models
from django.contrib.auth.models import User


class DiaryEntry(models.Model):

    CATEGORY_CHOICES = [
        ('Personal', 'Personal'),
        ('Study', 'Study'),
        ('Work', 'Work'),
        ('Ideas', 'Ideas'),
        ('Travel', 'Travel'),
        ('Other', 'Other'),
    ]

    MOOD_CHOICES = [
        ('Happy', '😊 Happy'),
        ('Excited', '🤩 Excited'),
        ('Calm', '😌 Calm'),
        ('Neutral', '😐 Neutral'),
        ('Sad', '😔 Sad'),
        ('Angry', '😡 Angry'),
        ('Tired', '😴 Tired'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='diary_entries'
    )

    title = models.CharField(max_length=200)

    content = models.TextField()

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Personal'
    )

    mood = models.CharField(
        max_length=20,
        choices=MOOD_CHOICES,
        default='Neutral'
    )

    is_pinned = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_pinned', '-created_at']

    def __str__(self):
        return self.title