from django.urls import path
from .import views

urlpatterns = [
    path('',views.main),
    path('home/', views.index,name='index'),
    path('home/details/<int:id>',views.details),
    path('testing',views.testing),
    path('home/add',views.add),
    path('add_record',views.addrecord, name='addrecord'),
    path('delete/<int:id>/',views.deleterecord, name='deleterecord'),
    # path('home/update',views.update)
    path('update/<int:id>/',views.updaterecord, name='update')

]