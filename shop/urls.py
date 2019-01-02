from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.quotes, name='index'),
    path('quotes/', views.quotes, name='quotes'),
    path('quote_edit/<int:quote_id>/', views.quotes, name='quote_edit'),
]
