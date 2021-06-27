from django.shortcuts import render


def homePage(request):
    return render(request, 'products/home.html')


def browsePage(request):
    return render(request, 'products/browse.html')
