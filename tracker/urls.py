from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('complete/<int:habit_id>/', views.complete_habit, name='complete_habit'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
