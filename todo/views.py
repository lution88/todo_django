from django.shortcuts import render

from todo.models import Todo


def todo_list(request):
    todo = Todo.objects.filter(complete=False)
    return render(request, 'todo_list.html', {'todo':todo})
