from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

from .forms import UserForm, CustomerForm


def index(request):
    return render(request, 'users/index.html')


@unauthenticated_user
def registerPage(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        customer_form = CustomerForm(request.POST)

        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            customer = customer_form.save(commit=False)
            customer.user = user

            request.session['username'] = user_form.cleaned_data.get('username')

            customer.save()
            return redirect('success')
    else:
        user_form = UserForm()
        customer_form = CustomerForm()

    setplaceholders(user_form)
    setplaceholders(customer_form)

    customer_form.fields['mobile'].widget.attrs['placeholder'] = 'Mobile number'

    context = {'user_form': user_form, 'customer_form': customer_form}
    return render(request, 'users/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users:profile')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    return redirect('users:login')


def successPage(request):
    username = request.session['username']
    messages.success(request, 'Registration successful ' + username)

    return render(request, 'users/success.html')


@login_required(login_url='users:login')
def profilePage(request):
    return render(request, 'users/account/account.html')


@login_required(login_url='users:login')
def addressPage(request):
    return render(request, 'users/account/address.html')


def setplaceholders(form):
    for field in form.fields:
        form.fields[field].widget.attrs['placeholder'] = form.fields[field].label
