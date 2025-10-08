from django.urls import path
from . import views

app_name = "polls"  # <--- This is the namespace

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),  # <--- name must match
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    path("<int:pk>/vote/", views.vote, name="vote"),
]
