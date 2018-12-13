from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Category, Product
import datetime


@login_required
def index(request):
    products = Product.objects.filter(deleted=False).order_by('-id')[:30]
    data = { 'products': products }
    return render(request, 'products/products.html', data)


@login_required
def product_edit(request,product_id=0):
    product = None
    try:
        product = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        product = Product()
        product.id = 0
    data = { 'product': product }
    return render(request, 'products/product_edit.html', data)


@login_required
def product_save(request):
    product_id = request.POST.get('product_id', 0)
    next = request.POST.get('next', 'list')
    if request.method == 'POST':
        product = Product()
        if int(product_id) > 0:
            product.id = product_id
        product.form(request.POST)
        product.user = request.user
        if product.is_valid():
            product.save()
            if next == 'add':
                return redirect('products:product_edit', 0)
            return redirect('products:index')
    return redirect('products:product_edit', product_id)


@login_required
def product_delete(request):
    product_id = request.POST.get('product_id', 0)
    if request.method == 'POST':
        try:
            product = Product.objects.get(id=product_id)
            product.deleted = True
            product.save()
        except ObjectDoesNotExist:
            product = None
    return redirect('products:index')


@login_required
def categories(request):
    categories = Category.objects.filter(deleted=False).order_by('-id')[:30]
    data = { 'categories': categories }
    return render(request, 'products/categories.html', data)


@login_required
def category_edit(request,category_id=0):
    category = None
    try:
        category = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
        category = Category()
        category.id = 0
    data = { 'category': category }
    return render(request, 'products/category_edit.html', data)


@login_required
def category_save(request):
    category_id = request.POST.get('category_id', 0)
    next = request.POST.get('next', 'list')
    if request.method == 'POST':
        category = Category()
        if int(category_id) > 0:
            category.id = category_id
        category.form(request.POST)
        category.user = request.user
        if category.is_valid():
            category.save()
            if next == 'add':
                return redirect('products:category_edit', 0)
            return redirect('products:categories')
    return redirect('products:category_edit', category_id)


@login_required
def category_delete(request):
    category_id = request.POST.get('category_id', 0)
    if request.method == 'POST':
        try:
            category = Category.objects.get(id=category_id)
            category.deleted = True
            category.save()
        except ObjectDoesNotExist:
            category = None
    return redirect('products:categories')
