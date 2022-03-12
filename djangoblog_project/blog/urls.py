from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # path('<int:pk>/', views.PostView.as_view(), name='post'),
    path('<slug:slug>/', views.PostView.as_view(), name='post'),
    
    path('', views.PostListView.as_view(), name='index'),
]