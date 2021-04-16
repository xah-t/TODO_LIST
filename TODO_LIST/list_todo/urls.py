from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
router = DefaultRouter()
router.register(r'notemethod3', views.NotesViewSet, basename='method3')

app_name = 'list_todo'
urlpatterns = [
    #path('notemethod1/', views.NotesView.as_view(), name='notemethod-1'),
    #path('notemethod2/', views.Notesgen1View.as_view(), name='notemethod-2'),
    #path('notemethod2/detail/<int:pk>/', views.Notesgen1DetailView.as_view(), name='notemethod-2Detail'),
    path('', include(router.urls))
]