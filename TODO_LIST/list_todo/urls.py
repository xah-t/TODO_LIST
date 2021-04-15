from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'list_todo'
urlpatterns = [
    path('notemethod1/', views.NotesView.as_view(), name='notemethod-1'),
]