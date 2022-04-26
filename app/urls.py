from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('add/', views.add_note, name= 'add'),
    path('detail/<int:pk>/', views.detail_nots, name= 'detail'),
    path('delete/<int:pk>/', views.delete_note, name= 'delete'),
]
