from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
    path('browse_fields/<str:client_id>/', views.browse_fields, name='browse_fields'),
    path('browse_clients/', views.browse_clients, name='browse_clients'),
    path('browse_channel_partners/', views.browse_channel_partners, name='browse_channel_partners'),
    path('client/<int:client_id>/update_field/<str:pk>/', views.update_field, name='update_field'),
    path('client/<str:client_id>/delete_field/<str:pk>/', views.delete_field, name='delete_field'),
    path('client/<int:client_id>/create_field/', views.create_field, name='create_field'),
]