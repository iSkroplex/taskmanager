from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DeleteView, DetailView



def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})\
        
        
class TaskDetailView(DetailView):
    template_name = 'main/task-detail.html'
    model = Task
    context_object_name = 'task'
    

class TaskDeleteView(DeleteView):
    success_url = '/'
    model = Task
    template_name = 'main/task-delete.html'
    



def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else: 
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

