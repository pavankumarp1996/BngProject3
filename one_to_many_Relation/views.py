from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
import datetime
from datetime import datetime




def pavan(request):
    form = timezone.now()
    return render(request, 'template/base.html', {'form':form})




