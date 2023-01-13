from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
from . import views
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority  = forms.IntegerField(label="priority ",min_value=7, max_value=10)
tasksli = ["foo", "bar", "doe"]

def index(request):
    if "tasks" not in request.session:
      request.session["tasks"] = []
    return render(request, "tasks/index.html",{
        "tasks":request.session["tasks"]
    })

def add(request):

    if request.method == "POST" :
        form = NewTaskForm(request.POST)
        if form.is_valid() :
            task = form.cleaned_data['task']
            request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/add.html", {
                "form":form
            })
    return render(request, "tasks/add.html",{
        "form":NewTaskForm()
    })

