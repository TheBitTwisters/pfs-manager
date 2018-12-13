from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('product_edit/<int:product_id>/', views.product_edit, name='product_edit'),
    path('product_save', views.product_save, name='product_save'),
    path('product_delete', views.product_delete, name='product_delete'),
    path('categories/', views.categories, name='categories'),
    path('category_edit/<int:category_id>/', views.category_edit, name='category_edit'),
    path('category_save/', views.category_save, name='category_save'),
    path('category_delete/', views.category_delete, name='category_delete'),
]
