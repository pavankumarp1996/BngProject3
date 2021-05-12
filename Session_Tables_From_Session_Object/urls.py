from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.Add_View),
    url(r'^display/$',views.display_View),






]