from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class NotesSerializer(serializers.ModelSerializer):
    """Заметки"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)



class NoteEditorSerializer(serializers.ModelSerializer):
    """Добавление и изменение заметки"""
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ['date_add', 'author', ]