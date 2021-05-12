from django.shortcuts import render

def Session(request):
    count=request.session.get('count',0)
    newcount = count+1
    request.session['count'] = newcount
    request.session.set_expiry(20)
    # print(request.session.get_expiry_age())
    # print(request.session.get_expiry_date())
    return render(request,'Session_Management_1/count.html',{'count':newcount})




    # print(request.session.get_expiry_age())
    # print(request.session.get_expiry_date())
    # return render(request,'Session_Management_1/session.html',{'count':newcount})




