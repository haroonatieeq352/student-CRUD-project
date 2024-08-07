from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.Home, name='home'),
    path('add/', views.Add_Student, name='add'),
    path('update/<int:id>/', views.Update_Student, name='update'),
    path('delete/<int:id>/', views.Delete_Student, name='delete'),
    path('search/', views.Search, name='search'),
    path('', views.Login, name='login'),
    path('signup/', views.Signup, name='signup'),
]