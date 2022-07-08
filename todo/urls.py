from django.urls import path

from todo.views import todo_list, todo_detail

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('<int:pk>/', todo_detail, name='todo_detail'),

]
