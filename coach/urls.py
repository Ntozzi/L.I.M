from django.urls import path
from . import views

app_name = 'coach' # for good practice

urlpatterns = [
    path('', views.coaches, name = 'coaches'),
    ]

