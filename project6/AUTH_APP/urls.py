from django.urls import path
from . import views


urlpatterns = [
    path('su/', views.signupView, name= 'signup_url'),
    path('log/', views.loginView, name= 'login_url'),
    path('lot/', views.logoutView, name= 'logout_url')
]