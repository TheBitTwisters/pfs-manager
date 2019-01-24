from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.list, name='index'),
    path('json/', views.json, name='json'),
    path('list/', views.list, name='list'),
    path('list/<str:category>/', views.list, name='list'),
    path('edit/<str:category>/<int:object_id>/', views.edit, name='edit'),
    path('save/<str:category>/', views.save, name='save'),
    path('delete/<str:category>/', views.delete, name='delete'),
]
