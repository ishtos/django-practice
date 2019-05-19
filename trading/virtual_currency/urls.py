from django.urls import path

from . import views


app_name = 'virtual_currency'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
