from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Note(models.Model):
    """Заметки  со статусом"""
    STATUSES = (
        (0, "Active"),
        (1, "Hold"),
        (2, "Done"),
    )

    title = models.CharField(default="", max_length=255)
    message = models.TextField(default="", blank=True)
    date_add = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)
    author = models.ForeignKey(User, related_name='authors', on_delete=models.PROTECT, blank=True)
    note_status = models.IntegerField(default=0, choices=STATUSES, verbose_name='Статус дела')
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.message
