from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('add/', views.add_new, name='add_new'),
    path('index/<int:id>', views.index, name='index'),
    path('index/<slug:slug>', views.index_slug, name='index_slug'),
    path('view/', views.view, name='view'),
    path('view/delete/<int:id>', views.delete_post, name='delete_post'),
    path('view/edit/<int:id>', views.edit, name='edit'),
    path('search/', views.search, name='search'),
]
