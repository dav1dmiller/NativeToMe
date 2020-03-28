from django.urls import path

app_name = 'accounts'

from . import views
urlpatterns = [
    path('login.html/', views.loginView),
    path('register.html/', views.registerView)
]