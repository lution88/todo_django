from django.shortcuts import render, redirect

from todo.forms import TodoForm
from todo.models import Todo


def todo_list(request):
    todo = Todo.objects.filter(complete=False)
    return render(request, 'todo/todo_list.html', {'todo':todo})


def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo':todo})


def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    form = TodoForm()
    return render(request, 'todo/todo_post.html', {'form': form})


def todo_edit(request, pk):
    todo = Todo.objects.get(pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance='todo')
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo-list')
    form = TodoForm(instance=todo)
    return render(request, 'todo/todo_post.html', {'form':form})