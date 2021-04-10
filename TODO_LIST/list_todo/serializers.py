from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class AuthorSerializer(serializers.ModelSerializer):
    """Автор статьи"""

    class Meta:
        model = User
        fields = ('id', 'username', 'date_joined')


class NotesSerializer(serializers.ModelSerializer):
    """Заметки"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Note
        fields = ('id', 'title', 'message', 'date_add', 'author', )


class NoteEditorSerializer(serializers.ModelSerializer):
    """Добавление и изменение заметки"""
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ['date_add', 'author', ]