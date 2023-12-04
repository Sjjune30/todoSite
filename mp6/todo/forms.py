from django import forms

from todoApp.models import todo


class Todo(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['task', 'priority', 'date']
