from django.urls import path
from .views import subscription_view, delete_subscription, undo_last_delete

urlpatterns = [
    path('', subscription_view, name='home'),
    path('delete/<int:pk>/', delete_subscription, name='delete_subscription'),
     path('undo_last_delete/', undo_last_delete, name='undo_last_delete'),
]
