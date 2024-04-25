from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.template import loader

from .forms import ProductForm


def home(request):
    return HttpResponse("Hello world!")

def index(request):
    return render(request, "index.html")

def productRegistration(request):

    if request.method == "POST":

        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")

    else:
        form = ProductForm()

    return render(request, "ingredient_registration.html", {"form": form})