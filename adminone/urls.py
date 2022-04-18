from pydoc import visiblename
from django.urls import path
from .import views
urlpatterns=[
    path('home',views.fnHome,name='home'),
    path('login',views.fnLogin,name='login'),
    path('plumb',views.fnPlumb,name='plumb'),
    path('offer',views.fnoffer,name='offer'),
    path('sign',views.fnsign,name='sign'),
    path('electrc',views.fnElectrc,name='electrc'),
    path('const',views.fnconst,name='const'),
    path('paint',views.fnpaint,name='paint'),
    path('homee',views.fnhomee,name='homee')
]