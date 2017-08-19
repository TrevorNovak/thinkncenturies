from django.utils import timezone
from django.db import models


class Post(models.Model):
    FICTION = 'fiction'
    NONFICTION = 'nonfiction'
    POETRY = 'poetry'
    ESSAY = 'essay'

    GENRE_CHOICES = (
        (FICTION , 'Fiction'),
        (NONFICTION , 'Noniction'),
        (POETRY , 'Poetry'),
        (ESSAY , 'Essay'),
    )

    genre = models.CharField(
        default='Undefined',
        choices=GENRE_CHOICES,
        max_length=255,
    )
    title = models.CharField(
        default='',
        max_length=255,
    )
    author = models.CharField(
        default='',
        max_length=255,
    )
    body = models.TextField(
        default='',
        blank=False,
    )
    created_on = models.DateTimeField(
        default=timezone.now,
    )

    def __str__(self):
        return self.title
