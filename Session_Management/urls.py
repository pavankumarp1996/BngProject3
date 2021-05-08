from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.Name),
    url(r'^age/$', views.Age),
    url(r'^GF/$', views.GF),
    url(r'^result',views.result_View),




]