from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('success', views.successPage, name='success'),
    path('profile', views.profilePage, name='profile'),
    path('edit', views.editInfo, name='editInfo'),
    path('changePassword', views.changePasswordPage, name='changePassword'),
    path('deleteAccount', views.deleteAccountPage, name='deleteAccount'),
    path('logout', views.logoutUser, name='logout'),
    path('orders', views.ordersPage, name='orders'),
    path('orders/details/<int:order_id>',
         views.orderDetails, name='order-details')
]
