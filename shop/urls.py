from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.quotes, name='index'),
    path('quotes/', views.quotes, name='quotes'),
    path('quote_edit/<int:quote_id>/', views.quote_edit, name='quote_edit'),
    path('quote_save', views.quote_save, name='quote_save'),
    path('quote_delete', views.quote_delete, name='quote_delete'),
]
