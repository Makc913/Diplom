from django.urls import path

from . import views

urlpatterns = [
    path('', views.start ),
    path('all_users/', views.all_user),
    path('user/<int:user_id>/', views.pers_user),
]
