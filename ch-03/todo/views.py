from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def todo_list(request: HttpRequest):
    # todos = Todo.objects.filter(complete=False)
    todos = get_list_or_404(Todo, complete=False)
    return render(request, 'todo/todo_list.html', {'todos': todos})


def todo_detail(request: HttpRequest, id):
    todo = get_object_or_404(Todo, pk=id)
    response = "todo_detail: id %d, %s" % (id, todo.title)
    return render(request, 'todo/todo_detail.html', {'todo': todo})


def todo_post(request: HttpRequest):
    print("[todo_post]: ")
    if request.method == "POST":
        print("[todo_post]: POST")
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        print("[todo_post]: GET")
        form = TodoForm()

    return render(request, 'todo/todo_post.html', {'form': form})

def todo_edit(request: HttpRequest, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == "POST":
        print("[todo_edit]: post, id %d" % id)
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todo/todo_post.html', {'form': form})

def done_list(request: HttpRequest):
    print("[done_list]")
    todos = Todo.objects.filter(complete=True)
    return render(request, 'todo/todo_complete.html', {'todos': todos})

def todo_done(request: HttpRequest, id):
    print("[todo_done] id %d" % id)
    todo = Todo.objects.get(pk=id)
    todo.complete = True
    todo.save()
    return redirect('todo_list')

