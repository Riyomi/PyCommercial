from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda req: redirect('/home/')),
    path('admin/', admin.site.urls),
    path('account/', include('users.urls', namespace='users')),
    path('home/', include('products.urls', namespace='products'))
]
