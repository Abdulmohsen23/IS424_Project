from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth
from .forms import ItemCreationForm, ItemUpdationForm, RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import Item,Own

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('items')  
    else:
        form = RegistrationForm()
    return render(request, 'IMS/register.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('items')  
    else:
        form = LoginForm()
    return render(request, 'IMS/login.html', {'form': form})

def log_out(request):
    auth.logout(request)
    
    return redirect("log_in")


@login_required(login_url='log_in')
def items(request):
    registered_only = request.GET.get('registered')
    items=Item.objects.all()
    if registered_only:
        final_items=[]
        for item in items:
            if Own.objects.filter(user=request.user, item=item).exists():
                final_items.append(item)
    else:
        final_items=items
    return render(request, 'IMS/items.html', {'items': final_items, 'registered_only': registered_only})


@login_required(login_url='log_in')
def create_item(request):
    if request.method == 'POST':
        form = ItemCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items')
        else:
            print(form.errors) 
    else:
        form = ItemCreationForm()
    return render(request, 'IMS/create_item.html', {'form': form})

# - Update an Event

@login_required(login_url='log_in')
def update_item(request, pk):

    item = Item.objects.get(id=pk)

    form = ItemUpdationForm(instance=item)

    if request.method == 'POST':

        form = ItemUpdationForm(request.POST, instance=item)

        if form.is_valid():

            form.save()

            return redirect("items")
        
    context = {'form':form}

    return render(request, 'IMS/update_item.html', context=context)


@login_required(login_url='log_in')
def delete_item(request, pk):
    record = Item.objects.get(id=pk)
    record.delete()
    return redirect("items")

@login_required(login_url='log_in')
def view_item(request, pk):

    item = Item.objects.get(id=pk)
    registered = Own.objects.filter(user=request.user, item=item)
    context = {'item':item, 'registered':registered}

    return render(request, 'IMS/view_item.html', context=context)


@login_required(login_url='sign_in')
def register_item(request, item_id):
    item = Item.objects.get(id=item_id)
    registration = Own.objects.filter(user=request.user, item=item)
    if registration.exists():
        registration.delete()
    else:
        Own.objects.create(user=request.user, item=item)

    return redirect('items')