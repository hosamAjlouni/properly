from django.urls import path
from . import views

app_name = 'leases'

urlpatterns = [
    path('all/', views.all, name='all'),
    path('active/', views.active, name='active'),
    path('add/', views.add, name='add'),
    path('add/<int:unit_id>/', views.add, name='add')
]