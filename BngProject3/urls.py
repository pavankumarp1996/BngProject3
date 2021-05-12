"""BngProject3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from one_to_many_Relation import views
from Django_Templates import views
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('pavan',views.pavan),
    url(r'^pavan',include('Django_Templates.urls')),
    url(r'^home',include('Template_Inheritence.urls')),
    url(r'^Cookie',include('session_management_Authentication.urls')),
    url(r'^Cookie',include('Session_Management.urls')),
    url(r'^session',include('Session_Management_1.urls')),
    url(r'^Forms',include('Session_Forms.urls')),
    url(r'^Tables',include('Session_Tables_From_Session_Object.urls')),





]

