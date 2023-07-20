from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('characters/', views.characters_index, name='characters_index'),
  path('characters/<int:character_index>/', views.characters_detail, name='characters_detail'),
  path('fighters/', views.fighters_index, name='index'),
  path('fighters/<int:fighter_id>/', views.fighters_detail, name='detail'),
  path('fighters/create/', views.FighterCreate.as_view(), name='fighters_create'),
  path('fighters/<int:pk>/update/', views.FighterUpdate.as_view(), name='fighters_update'),
  path('fighters/<int:pk>/delete/', views.FighterDelete.as_view(), name='fighters_delete'),
  path('stages/', views.stages_index, name='stages_index'),
  path('stages/<int:stage_id>/', views.stages_detail, name='stages_detail'),
  path('stages/create/', views.StageCreate.as_view(), name='stages_create'),
  path('stages/<int:pk>/update/', views.StageUpdate.as_view(), name='stages_update'),
  path('stages/<int:pk>/delete/', views.StageDelete.as_view(), name='stages_delete'),
]

 # path('fighters/<int:fighter_id>/add_stage', views.add_stage, name='add_stage'),