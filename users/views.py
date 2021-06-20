from django.shortcuts import render

from .forms import CreateUserForm


def index(request):
    return render(request, 'users/index.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'users/register.html', context)
