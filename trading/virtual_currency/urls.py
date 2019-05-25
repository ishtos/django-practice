from django.urls import path

from . import views


app_name = 'virtual_currency'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
