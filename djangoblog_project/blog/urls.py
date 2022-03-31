from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # path('<int:pk>/', views.PostView.as_view(), name='post'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('new/', views.CreatePostView.as_view(), name='post_new'),
    path('<slug:slug>/', views.PostView.as_view(), name='post_detail'),
    path(
        'post/<slug:slug>/edit/', views.PostUpdateView.as_view(), 
        name='post_edit'
    ),
    path(
        'post/<slug:slug>/remove/', views.PostDeleteView.as_view(), 
        name='post_remove'
    ),
    path(
        'post/<int:pk>/comment/', views.add_comment_to_post, 
        name='add_comment_to_post'
    ),
    path(
        'comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'
    ),
]