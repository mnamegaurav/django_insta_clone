from django.urls import path
from core.views import (
    HomeFeedView,
    LikedPostsView,
    PostCreateView,
    PostDeleteView,
    PostsExploreView,
    PostsSavedView,
    PostView,
    FollowDoneVideo,
    UnfollowDoneVideo,
    PostCommentView,
    PostLikeView,
    PostDislikeView,
    PostSaveView,
    )
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('feed/', login_required(HomeFeedView.as_view()), name='home_feed_view'),
    path('post/liked/', login_required(LikedPostsView.as_view()), name='liked_posts_view'),
    path('post/explore/', login_required(PostsExploreView.as_view()), name='posts_explore_view'),
    path('post/saved/', login_required(PostsSavedView.as_view()), name='posts_saved_view'),
    
    path('post/<int:id>/', login_required(PostView.as_view()), name='post_view'),
    path('post/save/<int:id>/', login_required(PostSaveView.as_view()), name='post_save_view'),
    path('post/create/', login_required(PostCreateView.as_view()), name='post_create_view'),
    path('post/delete/<int:id>/', login_required(PostDeleteView.as_view()), name='post_delete_view'),
    
    path('post/like/<int:id>/', login_required(PostLikeView.as_view()), name='post_like_view'),
    path('post/dislike/<int:id>/', login_required(PostDislikeView.as_view()), name='post_dislike_view'),

    path('post/comment/<int:id>/', login_required(PostCommentView.as_view()), name='post_comment_view'),

    path('follow/done/', login_required(FollowDoneVideo.as_view()), name='follow_done_view'),
    path('unfollow/done/', login_required(UnfollowDoneVideo.as_view()), name='unfollow_done_view'),
]