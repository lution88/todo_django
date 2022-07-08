from django.urls import path

from todo.views import todo_list, todo_detail, todo_post, todo_edit

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('<int:pk>/', todo_detail, name='todo_detail'),
    path('post/', todo_post, name='todo_post'),
    path('<int:pk>/edit/', todo_edit, name='todo_edit'),
]
