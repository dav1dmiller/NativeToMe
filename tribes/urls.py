from django.urls import path

app_name = 'tribes'

from . import views
urlpatterns = [
    path('tribeHomePage.html/', views.tribeHomePage),
    path('tribeCreatePage.html/', views.tribeCreate),
    path('tribeSearchPage.html/', views.tribeSearch),
]