import datetime
from main.models import Item
from main.forms import ItemForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/main/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'app_name': 'Kepomon',
        'name': request.user.username,
        'class': 'PBP A',
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        amount = form.cleaned_data['amount']
        messages.success(request, f"Berhasil menyimpan {amount} item pada aplikasi ini")
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form, 'app_name': 'Kepomon', 'class': 'PBP A'}
    return render(request, "create_item.html", context)

@login_required(login_url='/main/login')
def delete_item(request, id) :
    item = Item.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def increment_item(request, id) :
    item = Item.objects.get(id=id)
    item.amount += 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrement_item(request, id) :
    item = Item.objects.get(id=id)
    item.amount -= 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response