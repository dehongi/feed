from django.urls import path

from . import views

app_name = "feed"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("post/create/", views.PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
]
