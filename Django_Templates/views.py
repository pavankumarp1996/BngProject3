from django.shortcuts import render

def home(request):
    return render(request, 'template/template.html')

