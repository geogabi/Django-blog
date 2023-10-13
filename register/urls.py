from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_usr, name='login_usr'),
    path('logout/', views.log_out, name='log_out'),
]