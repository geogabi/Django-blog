from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('add/',views.adauga, name='adauga'),
    path('<int:id>',views.index,name='index'),
    path('<str:slug>',views.index_slug,name='index_slug'),
    path('view/',views.view, name='view'),
    path('view/delete/<int:id>', views.delete_post, name='delete_post'),
    path('view/editare/<int:id>', views.editare, name='editare'),
    path('search/<str:text>',views.filtru),
]