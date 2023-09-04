from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('add/',views.adauga, name='adauga'),
    path('<int:id>',views.index,name='index'),
    path('view/',views.view, name='view'),
    path('view/delete/<int:id>', views.delete_post, name='delete_post'),
    path('view/edit/<int:id>', views.edit_post, name='edit_post'),

]