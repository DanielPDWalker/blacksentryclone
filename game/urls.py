from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.game, name='game'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('resurrect/', views.resurrect, name='resurrect'),
    path('namechanger/', views.namechanger, name='namechanger')
]