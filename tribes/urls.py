from django.urls import path

app_name = 'tribes'

from . import views
urlpatterns = [
    path('tribeHomePage.html/', views.tribeHomePage),
]