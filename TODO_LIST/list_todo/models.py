from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Note(models.Model):
    """Заметки со статусом"""
    STATUSES = (
        (0, "Активно"),
        (1, "Ожидание"),
        (2, "Выполнено"),
    )

    title = models.CharField(default="", max_length=255)
    message = models.TextField(default="", blank=True)
    date_add = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)
    author = models.ForeignKey(User, related_name='authors', on_delete=models.PROTECT, blank=True)
    note_status = models.IntegerField(default=0, choices=STATUSES, verbose_name='Статус дела')
    important = models.BooleanField(default=False)

    def __str__(self):

        return f'{self.message}.\nStatus: {self.get_note_status_display()}'


class nlist(models.Model):
    # это должно быть в сериалайзере
    """Лист с заметками"""

    def add_note(self):
        # это должно быть в сериалайзере
        """добавленине заметки"""
        pass

    def del_note(self):
        # это должно быть в сериалайзере
        """удаление заметки"""
        pass

    def edit_note(self):
        # это должно быть в сериалайзере
        """изменение заметки"""
        pass


