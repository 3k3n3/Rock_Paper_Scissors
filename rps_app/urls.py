from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("game/", views.game, name="game"),  # rename
    path("friend/", views.friend, name="friend"),
]
