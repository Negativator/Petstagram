from django.urls import path

from pets import views

urlpatterns=[
    path('', views.pet_all, name='pet_all'),
    path('details/<int:pk>/', views.pet_detail, name='pet_datails'),
    path('like/<int:pk>/', views.pet_like, name='pet_like'),
    path('delete/', views.pet_delete, name='delete'),
]