from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
import datetime


@login_required
def index(request):
    return render(request, 'shop/index.html')
