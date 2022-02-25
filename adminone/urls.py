from pydoc import visiblename
from django.urls import path
from . import views
urlpatterns=[
    path('home',views.fnHome,name='home'),
   
    path('login',views.fnLogin,name='login'),
    path('path',views.fnabout,name='about'),
    path('contact',views.fncontact,name='contact'),
    path('offer',views.fnoffer,name='offer'),
    path('sign',views.fnsign,name='sign'),
    path('path',views.fnmenu,name='menu'),
    path('crt',views.fncrt,name='crt'),
]