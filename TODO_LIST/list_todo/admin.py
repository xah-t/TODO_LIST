from django.contrib import admin
from .models import Note

# Register your models here.
admin.site.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # Поля в списке
    list_display = ('title', 'date_add', 'public', 'author', 'id', )
# Группировка поля в режиме редактирования
    fields = ('date_add', ('title', 'public'), 'message', 'author')
    # Поля только для чтения в режиме редактирования
    readonly_fields = ('date_add', )

    # Поиск по выбранным полям
    search_fields = ['title', 'message', ]


