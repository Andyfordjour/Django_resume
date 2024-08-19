from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job/<int:job_id>/', views.detail, name='detail'),
]