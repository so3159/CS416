from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm


def hw4(request):
    return HttpResponse("Hello, world! How are you?")


def index(request):
    tasks = Todo.objects.all()
    form = TodoForm()
    context = {'tasks': tasks, 'form': form}

    return render(request, 'hw4/index.html', context)


def update(request, id):
    # Get the product based on its id
    task = Todo.objects.get(id=id)
    # populate a form instance with data from the data on the database
    # instance=product allows to update the record rather than creating a new record when save method is called
    form = TodoForm(request.POST or None, instance=task)

    # check whether it's valid:
    if form.is_valid():
        # update the record in the db
        form.save()
        # after updating redirect to view_product page
        return redirect('index')

    # if the request does not have post data, render the page with the form containing the product's info
    return render(request, 'hw4/update.html', {'form': form})


def delete(request, id):
    task = Todo.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'hw4/delete.html', {'task': task})


def add(request):
    if request.method == "POST":
        form = TodoForm( request.POST)
        if form.is_valid():
            form.save()
    return redirect('index')


def completed(request, id):
    task = Todo.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('index')
