from django import forms

from todo.models import Todo


class TodoForm(forms.Form):
    class Meta:
        model = Todo
        fields = ('title','description','important')
