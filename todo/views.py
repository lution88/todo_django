from django.shortcuts import render

from todo.models import Todo


def todo_list(request):
    todo = Todo.objects.filter(complete=False)
    return render(request, 'todo_list.html', {'todo':todo})


def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo_detail.html', {'todo':todo})


