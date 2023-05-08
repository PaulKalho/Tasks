from rest_framework import serializers
from rest_framework.serializers import ValidationError

from .models import Todo, Group

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id',
            'title',
            'description',
            'groupId',
            'pos',
            'deadline'
        )

class GroupTodosSerializer(serializers.ModelSerializer):
    group_todo = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = (
            'id',
            'name',
            'group_todo'
        )
    
    def get_group_todo(self, instance):
        allTodos = Todo.objects.all()
        # Check if todos deadline is today, if yes put it in today
        for todo in allTodos:
            if todo.is_today == True:
                todo.groupId = Group.objects.get(id = 0)
                todo.save()
        # todos => Todos for each group
        todos = instance.group_todo.order_by('pos')
        return TodoSerializer(todos, many=True).data


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'id',
            'name'
        )