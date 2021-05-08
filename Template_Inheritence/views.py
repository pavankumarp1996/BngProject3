from django.shortcuts import render

def home(request):
    return render(request,'template/Home.html')

def Course(request):
    return render(request,'template/Course.html')

def Feedback(request):
    return render(request,'template/feedback.html')



