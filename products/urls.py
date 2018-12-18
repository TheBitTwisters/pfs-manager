from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.coffins, name='index'),
    path('coffins', views.coffins, name='coffins'),
    path('coffin_edit/<int:coffin_id>/', views.coffin_edit, name='coffin_edit'),
    path('coffin_save', views.coffin_save, name='coffin_save'),
    path('coffin_delete', views.coffin_delete, name='coffin_delete'),
    path('services', views.services, name='services'),
    path('service_edit/<int:service_id>/', views.service_edit, name='service_edit'),
    path('service_save', views.service_save, name='service_save'),
    path('service_delete', views.service_delete, name='service_delete'),
]
