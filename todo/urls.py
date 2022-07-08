from django.urls import path

from todo.views import todo_list

urlpatterns = [
    path('', todo_list, name='todo_list'),
]
