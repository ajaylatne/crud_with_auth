from django.urls import path
from .views import order_view, show_order, update_view, delete_view

urlpatterns = [path('order/', order_view, name="order_url"),
               path('all_orders/', show_order, name="all_order_url"),
               path('update/<int:pk>/', update_view, name="update_url"),
               path('delete/<int:pk>/', delete_view, name="delete_url")
               ]
