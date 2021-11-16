from django.urls import path
from . import views

urlpatterns = [
    path('', views.faqs, name='faqs'),
]