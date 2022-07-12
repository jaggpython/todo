from django.shortcuts import redirect, render
from .forms import *
from .models import *

def index(request):
    task=Task.objects.all()
    form=Taskform()

    if request.method=="POST":
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context={'task':task,'form':form}
    return render(request,'index.html',context)

def delete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect("/")

def update(request,pk):
    task=Task.objects.get(id=pk)
    form=Taskform(instance=task)

    if request.method=="POST":
        form=Taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")

    context={'form':form}
    return render(request,'update.html',context)

