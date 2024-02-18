from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *


def index(request):
    return redirect('access')


def login_view(request):
    return render(request, "login.html")


def login_submit(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('dashboard')  # Redirect to the dashboard
    else:
        return HttpResponse("Failure.")


@login_required(login_url="/login")
def access_view(request):
    print(request.user.username)
    try:
        person = Person.objects.get(first_name='Josh')
        personIRs = PersonIR.objects.filter(person=person)
    except Person.DoesNotExist:
        return HttpResponse("Person not found.")

    context = {'personIRs': personIRs}
    return render(request, "access.html", context)


@login_required(login_url="/login")
def requests_view(request):
    requests = Request.objects.all()
    context = {'requests': requests}
    return render(request, "requests.html", context)