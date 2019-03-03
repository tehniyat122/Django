from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('data', views.datafromlogin, name='data'),
    path('data/getdata', views.getdata, name='getdata'),
]
