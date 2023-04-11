from django.urls import path
from . import views


urlpatterns = [
    path('ad/', views.addstudentView, name= 'addstudent_url'),
    path('sh/', views.showstudentView, name='showstudent_url'),
    path('up/<int:pk>/', views.updatestudentView, name= 'updatestudent_url'),
    path('dl/<int:pk>/', views.deletestudentView, name= 'deletestudent_url')
]