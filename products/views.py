from django.shortcuts import render
from .forms import UserForm

def index(request):
    return render(request, "index.html")

def base(request):
    return render(request, "base.html")

def catalog(request):
    return render(request, "catalog.html")

def register(request):
    name = "sabina"
    current_day = "17.12.2023"
    form = UserForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])
        new_form = form.save()
    return render(request, 'register.html', locals())