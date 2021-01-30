from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.logout_view, name='logout'),
    path('logout/', views.register, name='register'),
    
]