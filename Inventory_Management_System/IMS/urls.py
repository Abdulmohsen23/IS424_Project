# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.items, name='items'),
    path('sign-up/', views.register, name='register'),
    path('sign-in/', views.log_in, name='log_in'),
    path("sign-out/", views.log_out, name='log_out'),
    path('items/', views.items, name='items'),
    path("create-item/", views.create_item, name='create_item'),
    path('update-item/<int:pk>', views.update_item, name='update_item'),
    path('view-item/<int:pk>', views.view_item, name='view_item'),
    path('delete-item/<int:pk>', views.delete_item, name="delete_item"),
    path('register-item/<int:item_id>/', views.register_item, name='register_item'),
    
]
