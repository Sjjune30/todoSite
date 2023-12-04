from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

from forms import Todo
from .models import todo


# Create your views here.

class homeview(ListView):
    model = todo
    template_name = 'Home.html'
    context_object_name = 'task'
class detailview(DetailView):
    model = todo
    template_name = 'details.html'
    context_object_name = 'task'
class deleteview(DeleteView):
    model = todo
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
class updateview(UpdateView):
    model = todo
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('task', 'priority', 'date')
    success_url = reverse_lazy('cbvhome')


def home(request):
    task1 = todo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = todo(task=name, priority=priority, date=date)
        task.save()
    return render(request, 'Home.html', {'task': task1})
def delete(request, task_id):
    task = todo.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')
def update (request, id):
    task = todo.objects.get(id=id)
    todoo = Todo(request.POST or None, instance=task)
    if todoo.is_valid():
        todoo.save()
        return redirect('/')
    return render(request, 'update.html', {'todoo': todoo, 'task': task})
