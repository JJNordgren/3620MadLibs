from django.urls import path
from . import views

app_name = "madlibs"

urlpatterns = [
    path("", views.home, name="home"),
    path("play/", views.play, name="play"),
    path("result/<int:submission_id>/", views.result, name="result"),
    path("submissions/", views.my_submissions, name="submissions"),
]
