from django.urls import path
from . import views

app_name = 'keygen' # for good practice

urlpatterns = [
    path('', views.keygens, name = 'keygens'),
    path('response/', views.response, name = 'response'),
    ]

