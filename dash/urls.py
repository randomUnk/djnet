from django.urls import path, include
from . import views

			
urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('table', views.table, name='table'),
    path('blank', views.blank, name='blank'),
    path('test', views.test, name='test'),
    path('data_entry', views.data_entry, name='data_entry'),  
    path('logout', views.logout, name='logout'),   
]




