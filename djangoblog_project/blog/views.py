from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import generic
from .forms import PostForm
from django.urls import reverse


# def index(request):
#     a = Post.objects.all()
#     output = ', '.join([post.title for post in a])
#     return HttpResponse(output)

# https://docs.djangoproject.com/en/4.0/intro/tutorial04/#use-generic-views-less-code-is-better

# Learn about cotect_object_name:
# https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/
class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts' # by default object_list

class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'currentPost'

class CreatePostView(generic.CreateView):
    # redirect_field_name = 'blog/index.html'
    template_name = 'blog/write.html'
    form_class = PostForm
    model = Post

    def get_success_url(self): # new
        return reverse('blog:index')

# Create your views here.
