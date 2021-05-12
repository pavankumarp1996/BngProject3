from django.shortcuts import render
from .forms import NameForm,AgeForm,GfForm


def Name_View(request):
    name = NameForm()
    return render(request,'Session_Forms/name.html',{'name':name})


def Age_View(request):
    name = request.get('name')
    request.session['name'] = name
    Age = AgeForm()
    return render(request,'Session_Forms/age.html',{'Age':Age})

def Gf_View(request):
    age = request.get('age')
    request.session['age'] = age
    Gf = GfForm()
    return render(request,'Session_Forms/GF.html',{'Gf':Gf})

def Result_View(request):
    Gf  = request.get('Gf')
    request.session['Gf'] = Gf
    return render(request,'Session_Forms/Result.html')



















