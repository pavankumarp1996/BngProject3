from django.conf.urls import url
from Django_Templates import views
from django.contrib import admin

urlpatterns = [

    url(r'^$',views.home),



]