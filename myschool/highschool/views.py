from django.urls import reverse_lazy
from django.views import generic

from .forms import PostForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = "highschool/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(published=True)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "highschool/post_detail.html"
    context_object_name = "post"


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "highschool/post_form.html"
    success_url = reverse_lazy("highschool:post-list")


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = "highschool/post_form.html"
    success_url = reverse_lazy("highschool:post-list")


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "highschool/post_confirm_delete.html"
    success_url = reverse_lazy("highschool:post-list")
