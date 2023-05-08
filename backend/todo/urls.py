
from django.urls import path, include

from .views import GroupTodoView, TodoView, GroupView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('struct', GroupTodoView, basename="struct")
router.register('group', GroupView, basename="group")

urlpatterns = [
    path('todos/todo/', TodoView.as_view(), name="todo"),
    path('todos/', include(router.urls))
]
