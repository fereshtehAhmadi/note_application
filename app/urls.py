from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('date/', views.home, name= 'date'),
    path('name/', views.home, name= 'name'),
    path('add/', views.add_note, name= 'add'),
    path('detail/<int:pk>/', views.detail_nots, name= 'detail'),
    path("edit/<int:pk>/", views.edit_note, name="edit"),
    path('delete/<int:pk>/', views.delete_note, name= 'delete'),
    path("home/<str:cats>/", views.category, name="category"),
]
