from django.urls import path
from .views import sign_up, login_view, logout_view

urlpatterns = [
    path('sign_up/', sign_up, name="sign_up_url"),
    path('login_view/', login_view, name="login_url"),
    path('logout_view/', logout_view, name='logout_url')
    ]
