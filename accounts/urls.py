from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.userRegister, name='userRegister')
]
