from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from .models import todoItem


# Create your views here.

def todoView(request):
    # return HttpResponse('Hello, this is the todo app view!');
    all_todo_items = todoItem.objects.all()
    return render(request, 'todo.html', 
    {
        'all_items': all_todo_items
    } )

def addTodo(request):
    # create a new todo object and save it
    # re-direct to same url client came form

    c=request.POST['content']
    new_item = todoItem(content=c)
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    # delete the todo item with this id

    item_to_delete = todoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    # re-direct to same url client came form   
    return HttpResponseRedirect('/todo/')
