from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Coffin, Service


@login_required
def coffins(request):
    coffins = Coffin.objects.filter(deleted=False).order_by('-id')[:30]
    data = { 'coffins': coffins }
    return render(request, 'products/coffins.html', data)


@login_required
def coffin_edit(request,coffin_id=0):
    coffin = None
    try:
        coffin = Coffin.objects.get(id=coffin_id)
    except ObjectDoesNotExist:
        coffin = Coffin()
        coffin.id = 0
    data = { 'coffin': coffin }
    return render(request, 'products/coffin_edit.html', data)


@login_required
def coffin_save(request):
    coffin_id = request.POST.get('coffin_id', 0)
    next = request.POST.get('next', 'list')
    if request.method == 'POST':
        coffin = Product()
        if int(coffin_id) > 0:
            coffin.id = coffin_id
        coffin.form(request.POST)
        coffin.user = request.user
        if coffin.is_valid():
            coffin.save()
            if next == 'add':
                return redirect('products:coffin_edit', 0)
            return redirect('products:coffins')
    return redirect('products:coffin_edit', coffin_id)


@login_required
def coffin_delete(request):
    coffin_id = request.POST.get('coffin_id', 0)
    if request.method == 'POST':
        try:
            coffin = Coffin.objects.get(id=coffin_id)
            coffin.deleted = True
            coffin.save()
        except ObjectDoesNotExist:
            coffin = None
    return redirect('products:coffins')


@login_required
def services(request):
    services = Service.objects.filter(deleted=False).order_by('-id')[:30]
    data = { 'services': services }
    return render(request, 'products/services.html', data)
