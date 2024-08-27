from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post
from .forms import PostForm

# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.order_by("-created_at")


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous"] = self.get_previous_object()
        print(self.get_previous_object())
        context["next"] = self.get_next_object()
        return context

    def get_previous_object(self):
        return (
            self.model.objects.filter(created_at__lt=self.object.created_at)
            .order_by("-created_at")
            .first()
        )

    def get_next_object(self):
        return (
            self.model.objects.filter(created_at__gt=self.object.created_at)
            .order_by("created_at")
            .first()
        )


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def get_success_url(self) -> str:
        return reverse("feed:post_list")

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().user
