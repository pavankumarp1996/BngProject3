from django.conf.urls import url
from Template_Inheritence import views


urlpatterns = [

    url(r'^$',views.home),
    url(r'^Course/$',views.Course),
    url(r'^feedback/$',views.Feedback),
]



