from django.urls import path
from core.views import (
    HomeFeedView,
    LikedPostsView,
    )
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('feed/', login_required(HomeFeedView.as_view()), name='home_feed_view'),
    path('liked/', login_required(LikedPostsView.as_view()), name='liked_posts_view'),
]