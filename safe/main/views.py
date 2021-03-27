from django.shortcuts import render
from .forms import walkrequestform

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
