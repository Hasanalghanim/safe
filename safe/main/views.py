from django.shortcuts import render, redirect
from main.forms import walkrequestform
from main.models import walkrequest


from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def home(request):
    form = walkrequestform()

    if request.method == "POST":
        form = walkrequestform(request.POST)
        if form.is_valid():
            form = form.save()
            data = "form saved"
        return render(request,'main/home.html', {'data':data, 'form':form })

    if request.method == "GET":
        form = walkrequestform()
        data = "do the form"
        return render(request,'main/home.html', {'data':data, 'form':form })



def dashboard(request):
    walk = walkrequest.objects.all()
    return render(request,'main/dashboard.html', {'walk':walk })


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'main/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'main/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match. '})
        else:
            login(request, user)
            return redirect('dashboard')
