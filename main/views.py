from django.shortcuts import render
from main.forms import ItemForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.urls import reverse
from main.models import Item
from django.contrib import messages

def show_main(request):
    items = Item.objects.all()

    context = {
        'app_name': 'Kepomon',
        'name': 'Muhammad Daffa\'I Rafi Prasetyo',
        'class': 'PBP A',
        'items': items
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        amount = form.cleaned_data['amount']
        messages.success(request, f"Berhasil menyimpan {amount} item pada aplikasi ini")
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form, 'app_name': 'Kepomon', 'class': 'PBP A'}
    return render(request, "create_item.html", context)
