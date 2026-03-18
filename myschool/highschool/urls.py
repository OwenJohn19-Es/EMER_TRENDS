from django.urls import path

from .views import (
    HighschoolLandingView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)

app_name = "highschool"

urlpatterns = [
    path("", HighschoolLandingView.as_view(), name="landing"),
    path("highschoolblog/", PostListView.as_view(), name="highschoolblog"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
