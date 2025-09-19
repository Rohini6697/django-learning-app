from django.urls import path
from .import views

urlpatterns = [
    path('',views.main),
    path('home/', views.index),
    path('home/details/<int:id>',views.details)
]