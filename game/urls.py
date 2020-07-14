from django.urls import path, urls
from . import views

urlpatterns = [
    path('', views.game, name='game'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    #url(r'^ajax/post/$', '')

]
