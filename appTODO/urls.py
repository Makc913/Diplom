from django.urls import path

from . import views

urlpatterns = [
    path('', views.start ),
    path('all_users/', views.all_users),
    path('user/<int:user_id>/', views.pers_user),
    path('create_task/', views.create_task),
    path('get_task_user/', views.get_task_user),
    path('create_category/', views.create_category),
    path('user_detail/', views.user_detail)
]