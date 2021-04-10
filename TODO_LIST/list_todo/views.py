from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import Note
from .serializers import NotesSerializer
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the list_todo index.")


class NotesView(APIView):
    """Заметки в листе"""

    def get(self, request):
        """получить заметки листа"""
        notes = Note.objects.filter(public=True).order_by('-date_add', 'title')

        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)
