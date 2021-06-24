from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import UserForm, CustomerForm


def index(request):
    return render(request, 'users/index.html')


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


def loginPage(request):
    if request.method == 'POST':
        request.POST.get('username')
        request.POST.get('username')

    return render(request, 'users/login.html')


def successPage(request):
    username = request.session['username']
    messages.success(request, 'Registration successful ' + username)

    return render(request, 'users/success.html')


def setplaceholders(form):
    for field in form.fields:
        form.fields[field].widget.attrs['placeholder'] = form.fields[field].label
