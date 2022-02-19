from django.urls import path
from . import views
urlpatterns=[
    path('home',views.fnHome,name='home'),
    path('',views.fnFirst,name='first'),
    path('login',views.fnLogin,name='login')
]