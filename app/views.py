from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

from app.forms import *

def djangoforms(request):
    data=NameForm()
    d={'data':data}
    if request.method=='POST':
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            name=form_data.cleaned_data['name']
            age=form_data.cleaned_data['age']
            email=form_data.cleaned_data['email']
            password=form_data.cleaned_data['password']
            gender=form_data.cleaned_data['gender']
            course=form_data.cleaned_data['course']
            address=form_data.cleaned_data['address']
            d1={'n':name,'a':age,'e':email,'p':password,'g':gender,'c':course,'ad':address}
            return render(request,"valid_data.html",d1)
    return render(request,"djangoforms.html",d)