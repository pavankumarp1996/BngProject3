from django.shortcuts import render

def Cookie_View(request):
    count = int(request.COOKIES.get('count',0))
    newcount = count+1
    responce=render(request,'Authentication/cooke.html',{'count':newcount})
#  this is temparary Cookies
    # responce.set_cookie('count',newcount)
    responce.set_cookie('count',newcount,max_age=180)
    return responce



