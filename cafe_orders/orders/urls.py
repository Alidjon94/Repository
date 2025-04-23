from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='orders-index'),
    path('create/', views.create_order, name='create-order'),
    path('edit/<int:order_id>/', views.edit_order, name='edit-order'),
    path('delete/<int:order_id>/', views.delete_order, name='delete-order'),
    path('status/<int:order_id>/', views.change_status, name='change-status'),
]
