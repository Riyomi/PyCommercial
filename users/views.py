from django.shortcuts import render, redirect

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

            customer.save()
            # TODO: add redirect here with correct namespace
            # return redirect('register:users')
    else:
        user_form = UserForm()
        customer_form = CustomerForm()

    context = {'user_form': user_form, 'customer_form': customer_form}
    return render(request, 'users/register.html', context)
