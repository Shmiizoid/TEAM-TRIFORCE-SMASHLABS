from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('fighters/', views.fighters_index, name='index'),
  path('fighters/<int:fighter_id>/', views.fighters_detail, name='detail'),
]

