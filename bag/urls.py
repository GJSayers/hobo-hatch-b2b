from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('edit/<item_id>/', views.edit_bag, name='edit_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]
