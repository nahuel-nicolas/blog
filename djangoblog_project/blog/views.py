from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Post, Comment
from django.views import generic
from .forms import PostForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# def index(request):
#     a = Post.objects.all()
#     output = ', '.join([post.title for post in a])
#     return HttpResponse(output)

# https://docs.djangoproject.com/en/4.0/intro/tutorial04/#use-generic-views-less-code-is-better

# Learn about cotect_object_name:
# https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/
class PostListView(generic.ListView):
    model = Post

class PostView(generic.DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class CreatePostView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', post.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_slug = comment.post.slug
    comment.delete()
    return redirect('blog:post_detail', post_slug)
