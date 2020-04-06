from django.urls import path

app_name = 'accounts'

from . import views
urlpatterns = [
    path('login.html/', views.loginView),
    path('logout.html/', views.logoutView),
    path('register.html/', views.registerView),
    path('userprofile.html/', views.registerView),
]