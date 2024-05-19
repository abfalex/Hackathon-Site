from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('participants/', views.participants, name='participants'),
    path('modules/', views.modules, name='modules'),
    path('manage_modules/', views.manage_modules, name='manage_modules'),
    path('module_details/<int:pk>/', views.module_details, name='module_details'),
    path('modules/edit/<int:module_id>/', views.edit_module, name='edit_module'),
    path('modules/delete/<int:module_id>/', views.delete_module, name='delete_module'),
    path('tasks/', views.manage_tasks, name='manage_tasks'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task')
]
