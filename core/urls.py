from django.urls import path
from core.views import (
    HomeFeedView,
    LikedPostsView,
    PostCreateView,
    PostDeleteView,
    PostsExploreView,
    PostView,
    )
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('feed/', login_required(HomeFeedView.as_view()), name='home_feed_view'),
    path('liked/', login_required(LikedPostsView.as_view()), name='liked_posts_view'),
    path('explore/', login_required(PostsExploreView.as_view()), name='posts_explore_view'),
    
    path('post/<int:id>/', login_required(PostView.as_view()), name='post_view'),
    path('post/create/', login_required(PostCreateView.as_view()), name='post_create_view'),
    path('post/delete/<int:id>/', login_required(PostDeleteView.as_view()), name='post_delete_view'),
]