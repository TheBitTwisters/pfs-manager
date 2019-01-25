from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.utils import timezone
from .models import Product
from logs.models import Log


@login_required
def json(request, category='coffin'):
    param_name = request.GET.get('name', '')
    param_category = request.GET.get('category', '')
    param_limit = int(request.GET.get('limit', 10))
    param_page = int(request.GET.get('page', 1))
    param_offset = param_limit * (param_page - 1)
    products = Product.objects.filter(deleted=False, name__icontains=param_name, category__contains=param_category).order_by('-id')[param_offset:param_limit]
    json_products = {}
    for product in products:
        json_products[product.id] = {
            'id': product.id,
            'category': product.category,
            'code': product.code,
            'name': product.name,
            'description': product.description,
            'design': product.design,
            'price': product.price
        }
    return JsonResponse({
        'products': json_products
    })


@login_required
def list(request, category='coffin'):
    products = Product.objects.filter(category=category, deleted=False).order_by('-id')[:30]
    if category == 'service':
        data = { 'services': products }
        template = 'products/services.html'
    else:
        data = { 'coffins': products }
        template = 'products/coffins.html'
    return render(request, template, data)


@login_required
def edit(request, category, object_id=0):
    product = None
    try:
        product = Product.objects.get(id=object_id)
    except ObjectDoesNotExist:
        product = Product()
        product.id = 0
        product.category = category
    if category == 'service':
        data = { 'service': product }
        template = 'products/service_edit.html'
    else:
        data = { 'coffin': product }
        template = 'products/coffin_edit.html'
    return render(request, template, data)


@login_required
def save(request, category):
    object_id = request.POST.get('object_id', 0)
    next = request.POST.get('next', 'list')
    action = 'create'
    if request.method == 'POST':
        product = Product()
        try:
            if int(object_id) > 0:
                product.id = object_id
                action = 'update'
                product.datetime_updated = timezone.now()
        except ValueError as e:
            product.id = 0
        product.category = category
        product.form(request.POST)
        product.user = request.user
        if product.is_valid():
            try:
                product.save()
                Log.objects.create(
                    object = 'Product:' + category,
                    object_id = product.id,
                    action = action,
                    user = request.user
                )
                if next == 'add':
                    return redirect('products:edit', category, 0)
                return redirect('products:list', category)
            except IntegrityError as e:
                product = None
    return redirect('products:edit', category, object_id)


@login_required
def delete(request, category):
    object_id = request.POST.get('object_id', 0)
    if request.method == 'POST':
        try:
            product = Product.objects.get(id=object_id)
            product.deleted = True
            product.datetime_deleted = timezone.now()
            product.save()
            Log.objects.create(
                object = 'Product:' + category,
                object_id = product.id,
                action = 'delete',
                user = request.user
            )
        except ObjectDoesNotExist:
            product = None
    return redirect('products:list', category)
