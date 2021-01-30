from django.urls import path
from . import views


app_name = 'contacts'

urlpatterns = [
    path('all/', views.all, name='all'),
    path('add/', views.add, name='add'),
    path('contact/<int:contact_id>/', views.contact, name='contact'),
]