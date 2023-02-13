from django.urls import path

from . import views

urlpatterns = [


   
    path('',views.addshow,name='addshow'),
    path('<str:pk>/', views.update, name="update"),
    path('delete/<str:pk>/', views.delete, name="delete"),
    path('deletedep/<str:pk>/', views.deletedep, name="deletedep"),


]