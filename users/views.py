from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from .decorators import unauthenticated_user
from .forms import UserForm, CustomerForm, EditUserInfoForm
from products.models import Order, OrderItem
from users.models import Customer


@unauthenticated_user
def registerPage(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        customer_form = CustomerForm(request.POST)

        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            customer = customer_form.save(commit=False)
            customer.user = user

            customer.save()

            user = authenticate(
                request, username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password1'])
            login(request, user)

            return redirect('products:home')
    else:
        user_form = UserForm()
        customer_form = CustomerForm()

    setplaceholders(user_form)
    setplaceholders(customer_form)

    customer_form.fields['mobile'].widget.attrs['placeholder'] = 'Mobile number'

    return render(request, 'users/register.html', {'user_form': user_form, 'customer_form': customer_form})


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('products:home')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    return redirect('users:login')


@login_required(login_url='users:login')
def profilePage(request):
    return render(request, 'users/account/account.html')


@login_required(login_url='users:login')
def editInfo(request):
    if request.method == 'POST':
        user_form = EditUserInfoForm(
            request.POST, instance=request.user)
        customer_form = CustomerForm(
            request.POST, instance=request.user.customer)

        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.is_active = True
            user.save()
            customer = customer_form.save(commit=False)
            customer.user = user

            request.session['username'] = user_form.cleaned_data.get(
                'username')

            customer.save()

            return redirect('users:profile')
    else:
        user_form = EditUserInfoForm(instance=request.user)
        customer_form = CustomerForm(instance=request.user.customer)

        # TODO: this doesn't work if the country code isn't in +xx format
        customer_form.fields['mobile'].widget.attrs['value'] = str(request.user.customer.mobile)[
            3:]

    setplaceholders(user_form)
    setplaceholders(customer_form)

    customer_form.fields['mobile'].widget.attrs['placeholder'] = 'Mobile number'

    return render(request, 'users/account/editInfo.html', {'user_form': user_form, 'customer_form': customer_form})


@login_required(login_url='users:login')
def deleteAccountPage(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2 and password1 and password2:
            customer = Customer.objects.get(id=request.user.customer.id)
            if check_password(password1, customer.user.password):
                user = User.objects.get(pk=request.user.id)
                user.delete()
                return redirect('products:home')
        else:
            messages.info(request, 'Passwords do not match.')

    return render(request, 'users/account/deleteAccount.html')


@login_required(login_url='users:login')
def changePasswordPage(request):
    if request.method == 'POST':
        newPassword1 = request.POST.get('newPassword1')
        newPassword2 = request.POST.get('newPassword2')
        if newPassword1 and newPassword2 and newPassword1 == newPassword2:
            user = Customer.objects.get(id=request.user.customer.id).user
            user.set_password(newPassword1)
            user.save()
            messages.success(request, 'Password succesfully updated.')
            request.user.set_password(newPassword1)
            update_session_auth_hash(request, user)
        else:
            messages.info(request, 'Passwords do not match.')

    return render(request, 'users/account/changePassword.html')


@login_required(login_url='users:login')
def ordersPage(request):
    orders = Order.objects.filter(
        customer=request.user.customer).order_by('-date_placed')
    paginator = Paginator(orders, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'users/account/orders.html', {'page_obj': page_obj})


def orderDetails(request, order_id):
    if request.user.is_authenticated:
        order = get_object_or_404(Order, pk=order_id,
                                  customer=request.user.customer)
    elif request.session['guest']:
        order = get_object_or_404(Order, pk=request.session['guest'])

    data = {
        'order': order,
        'items': OrderItem.objects.filter(order=order),
    }

    return render(request, 'users/orderDetails.html', {'data': data})


def setplaceholders(form):
    for field in form.fields:
        form.fields[field].widget.attrs['placeholder'] = form.fields[field].label
