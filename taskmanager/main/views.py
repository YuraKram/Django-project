from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def price(request):
    return render(request, 'main/price.html')


def feedback(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/feedback.html', {'title': 'Массаж', 'tasks': tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

