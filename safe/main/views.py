from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import walkrequestform
from main.models import walkrequest
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core import serializers
from django.http import JsonResponse
# Create your views here.


def home(request):
    form = walkrequestform()

    if request.method == "POST":
        form = walkrequestform(request.POST)
        data = "thank you"
        if form.is_valid():
            form = form.save()

        return render(request, 'main/home.html', {'form': form, "data": data})

    if request.method == "GET":
        form = walkrequestform()

        return render(request, 'main/home.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    walk = walkrequest.objects.all()
    if request.is_ajax():
        return render(request, 'main/dashboard.html', {'walk': walk})
    else:
        return render(request, 'main/dashboard.html', {'walk': walk})


@login_required(login_url='login')
def done(request):
    walk = walkrequest.objects.filter(completed=True)
    return render(request, 'main/done.html', {'walk': walk})


@login_required(login_url='login')
def walkdetails(request, walkrequest_pk):
    walk = get_object_or_404(walkrequest, pk=walkrequest_pk)
    if request.method == "GET":
        form = walkrequestform(instance=walk)
        return render(request, 'main/walkdetails.html', {'walk': walk, 'form': form})
    else:
        form = walkrequestform(request.POST, instance=walk)
        if form.is_valid():
            form.save()
        return redirect('dashboard')


def walkcompleted(request, walkrequest_pk):
    walk = get_object_or_404(walkrequest, pk=walkrequest_pk)
    if request.method == 'POST':
        walk.save()
    return redirect('dashboard')


def get(request):
    if request.is_ajax or request.method == "GET":
        walk = walkrequest.objects.filter(date_completed=None)
        data = serializers.serialize('json', walk, fields=(
            'name', 'phone', 'fromlocation', 'tolocation', 'timerecived', 'completed'))
        return HttpResponse(data, content_type="application/json")
    return HttpResponse({'message': 'Wrong Validation'}, status=400)


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'main/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'main/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match. '})
        else:
            login(request, user)
            return redirect('dashboard')


login_required(login_url='login')


def logoutuser(request):
    if request == "POST":
        logout(request)
    return redirect(home)
