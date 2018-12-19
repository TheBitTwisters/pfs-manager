from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Log
import datetime


@login_required
def index(request):
    logs = Log.objects.all().order_by('-id')[:100]
    data = { 'logs': logs }
    return render(request, 'logs/index.html', data)
