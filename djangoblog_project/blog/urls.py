from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # path('<int:pk>/', views.PostView.as_view(), name='post'),
    path('new/', views.CreatePostView.as_view(), name='post_new'),
    path('<slug:slug>/', views.PostView.as_view(), name='post_detail'),
    path('', views.PostListView.as_view(), name='post_list'),
]