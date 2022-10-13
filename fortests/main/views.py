from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

from django.http import HttpResponse

"""
def index(request):
    return HttpResponse("<h3>Hello, world!</h3>")


def about_us(request):
    return HttpResponse("<h3>About us!</h3>")"""


def index1(request):
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})


def examples(request):
    return render(request, 'main/examples.html')


def about_us1(request):
    return render(request, 'main/about.html')

'''
def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
'''