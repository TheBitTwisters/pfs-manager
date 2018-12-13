from django.urls import path
from . import views


app_name = 'materials'
urlpatterns = [
    path('', views.index, name='index'),
    path('deleted/', views.deleted, name='deleted'),
    path('edit/<int:material_id>/', views.edit, name='edit'),
    path('save/', views.save, name='save'),
    path('delete/', views.delete, name='delete'),
]
