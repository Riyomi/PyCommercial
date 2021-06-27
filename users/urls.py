from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('success', views.successPage, name='success'),
    path('account', views.profilePage, name='profile'),
    path('address', views.addressPage, name='address'),
    path('logout', views.logoutUser, name='logout')
]
