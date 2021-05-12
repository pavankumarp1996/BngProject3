from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.Name_View),
    url(r'^age/$',views.Age_View),
    url(r'^GF/$',views.Gf_View),
    url(r'^result/$',views.Result_View),

]



