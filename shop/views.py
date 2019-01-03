from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .models import Quote
from logs.models import Log


@login_required
def quotes(request):
    quotes = Quote.objects.filter(deleted=False).order_by('-id')[:30]
    data = { 'quotes': quotes }
    return render(request, 'shop/quotes.html', data)


@login_required
def quote_edit(request, quote_id=0):
    quote = None
    try:
        quote = Quote.objects.get(id=quote_id)
    except ObjectDoesNotExist:
        quote = Quote()
        quote.id = 0
    data = { 'quote': quote }
    return render(request, 'shop/quote_edit.html', data)


@login_required
def quote_save(request):
    quote_id = request.POST.get('quote_id', 0)
    action = 'create'
    if request.method == 'POST':
        quote = Quote()
        try:
            if int(quote_id) > 0:
                quote.id = quote_id
                action = 'update'
                quote.datetime_updated = timezone.now()
        except ValueError as e:
            quote.id = 0
        quote.form(request.POST)
        quote.user = request.user
        if quote.is_valid():
            quote.save()
            Log.objects.create(
                object = 'Quote',
                object_id = quote.id,
                action = action,
                user = request.user
            )
            return redirect('shop:quotes')
    return redirect('shop:quote_edit', quote_id)


@login_required
def quote_delete(request):
    quote_id = request.POST.get('quote_id', 0)
    if request.method == 'POST':
        try:
            quote = Quote.objects.get(id=quote_id)
            quote.deleted = True
            quote.datetime_deleted = timezone.now()
            quote.save()
            Log.objects.create(
                object = 'Quote',
                object_id = quote.id,
                action = 'delete',
                user = request.user
            )
        except ObjectDoesNotExist:
            quote = None
    return redirect('shop:quotes')
