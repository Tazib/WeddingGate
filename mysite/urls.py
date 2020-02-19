from django.urls import path
from . import views

urlpatterns = (
    path('', views.index, name='home'),
    path('test/', views.testFile),
    path('link/', views.testFile, name='link'),
    path('autogen/', views.autogen, name='autogen'),
    path('chuck/', views.chuck, name='chuck'),
    path('result/', views.result, name='result'),

)
