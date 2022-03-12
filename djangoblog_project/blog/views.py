from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import generic


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

# Create your views here.
