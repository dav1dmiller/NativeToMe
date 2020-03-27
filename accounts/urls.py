from django.urls import path
from django.contrib import admin

app_name = 'accounts'

from . import views
urlpatterns = [
    path('', views.loginView, name='login'),
    path('', views.registerView, name='register')
]