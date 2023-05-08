from django.contrib import admin

from .models import Todo, Group

# Register your models here.
class CustomTodoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = ('id', 'title', 'description', 'groupId', 'pos', 'deadline')

class CustomGroupAdmin(admin.ModelAdmin):
    model: Group
    list_display = ('id', 'name')

admin.site.register(Todo, CustomTodoAdmin)
admin.site.register(Group, CustomGroupAdmin)