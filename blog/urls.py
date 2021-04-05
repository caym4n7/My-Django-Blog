from . import views
from .views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostCategory
)
from django.urls import path

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('like/', views.like_post, name='like-post'),
    path('about/', views.about, name='blog-about'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/category/<slug:slug>/', PostCategory.as_view(), name='post_by_category'),
    #path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]

