from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .models import Material
from logs.models import Log


@login_required
def index(request):
    materials = Material.objects.filter(deleted=False).order_by('-id')[:30]
    data = { 'materials': materials }
    return render(request, 'materials/latest.html', data)


@login_required
def deleted(request):
    materials = Material.objects.filter(deleted=True).order_by('-id')[:30]
    data = { 'materials': materials }
    return render(request, 'materials/deleted.html', data)


@login_required
def edit(request, material_id=0):
    material = None
    try:
        material = Material.objects.get(id=material_id)
    except ObjectDoesNotExist:
        material = Material()
        material.id = 0
    data = { 'material': material }
    return render(request, 'materials/edit.html', data)


@login_required
def save(request):
    material_id = request.POST.get('material_id', 0)
    next = request.POST.get('next', 'list')
    action = 'create'
    if request.method == 'POST':
        material = Material()
        if int(material_id) > 0:
            material.id = material_id
            action = 'update'
            material.datetime_updated = timezone.now()
        material.form(request.POST)
        material.user = request.user
        if material.is_valid():
            material.save()
            Log.objects.create(
                object = 'Material',
                object_id = material.id,
                action = action,
                user = request.user
            )
            if next == 'add':
                return redirect('materials:edit', 0)
            return redirect('materials:index')
    return redirect('materials:edit', material_id)


@login_required
def delete(request):
    material_id = request.POST.get('material_id', 0)
    if request.method == 'POST':
        try:
            material = Material.objects.get(id=material_id)
            material.deleted = True
            material.datetime_deleted = timezone.now()
            material.save()
            Log.objects.create(
                object = 'Material',
                object_id = material.id,
                action = 'delete',
                user = request.user
            )
        except ObjectDoesNotExist:
            material = None
    return redirect('materials:index')
