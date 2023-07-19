from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('fighters/', views.fighters_index, name='index'),
  path('fighters/<int:fighter_id>/', views.fighters_detail, name='detail'),
  path('fighters/create/', views.FighterCreate.as_view(), name='fighters_create'),
  path('fighters/<int:pk>/update/', views.FighterUpdate.as_view(), name='fighters_update'),
  path('fighters/<int:pk>/delete/', views.FighterDelete.as_view(), name='fighters_delete'),
  path('fighters/<int:fighter_id>/add_stage', views.add_stage, name='add_stage'),
]

