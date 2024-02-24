from django.urls import path

from . import views

urlpatterns = [
    path('', views.start ),
    path('all_users/', views.all_user),
    path('user/<int:user_id>/', views.pers_user),
    path('create_task/', views.create_task),
    path('get_in_user/', views.get_in_user),
    path('get_task_user/', views.get_task_user),
]