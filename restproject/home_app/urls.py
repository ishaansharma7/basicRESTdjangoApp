from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.task_list, name='list'),
    path('detail/<int:pk>/', views.detail_list, name='detail'),
    path('create/', views.task_create, name='create'),
    path('update/<int:pk>/', views.task_update, name='update'),
]
