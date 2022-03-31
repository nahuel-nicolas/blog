from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import generic
from .forms import PostForm
from django.urls import reverse
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

class CreatePostView(LoginRequiredMixin, generic.CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    
    form_class = PostForm
    model = Post

    # def get_success_url(self): 
    #     return reverse('blog:index')

# Create your views here.
