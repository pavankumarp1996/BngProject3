from django.shortcuts import render

def Name(request):
    return render(request,'Session_Management/name.html')
def Age(request):
    name = request.GET['name']       # Read the data from the name.html
    responce =  render(request,'Session_Management/age.html')
    responce.set_cookie('name',name)
    return responce
def GF(request):
    age = request.GET['age']
    responce = render(request,'Session_Management/GF.html')
    responce.set_cookie('age',age)
    return responce
def result_View(request):
    gfname = request.GET['gfname']
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    responce = render(request,'Session_Management/result.html',{'gfname':gfname,'name':name,'age':age})
    return responce














