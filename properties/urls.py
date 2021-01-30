from django.urls import path
from . import views

app_name = 'properties'

urlpatterns = [
    path('all/', views.all, name='all'),
    path('property/<int:property_id>/', views.property, name='property'),
    path('property_add/', views.property_add, name='add'),
    path('property_edit/<int:property_id>', views.property_edit, name='edit'),
    path('units/', views.units, name='units'),
    path('unit_add/', views.unit_add, name='unit_add'),
    path('unit_add/<int:property_id>/', views.unit_add, name='unit_add'),
    path('unit/<int:unit_id>/', views.unit, name='unit'),
]