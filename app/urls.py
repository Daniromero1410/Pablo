from django.urls import path
from . import views 
urlpatterns=[
    path('', views.index, name='index'),
    path('list_ingenieria/',views.list_ingenierias,name='list_ingenieria')
]
    