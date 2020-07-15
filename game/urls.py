from django.urls import path
from . import views

urlpatterns = [
    path('', views.game, name='game'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('ressurect/', views.ressurect, name='ressurect')
]
