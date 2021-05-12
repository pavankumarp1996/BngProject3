from django.shortcuts import render
from . forms import AddForm

def Add_View(request):
    form = AddForm()
    if request.method == 'POST':
        name = request.POST['name']
        quntity = request.POST['quntity']
        request.session[name] = quntity
    return render(request,'Session_Tables_From_Session_Object/add.html',{'form':form})

def display_View(request):

    return render(request,'Session_Tables_From_Session_Object/display.html')





