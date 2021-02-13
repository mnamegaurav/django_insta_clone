from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Count
from django.contrib.auth import get_user_model

from core.models import Post, Follow, Like, Comment
from core.forms import PostCreateForm

User = get_user_model()

# Create your views here.
class HomeFeedView(View):
    template_name = 'core/feed.html'
    form_class = PostCreateForm

    def get(self, request, *args, **kwargs):
        all_posts = Post.objects.all()
        form = self.form_class()
        context = { 'all_posts': all_posts, 'form': form }
        return render(request, self.template_name, context=context)


class PostView(View):
    template_name = 'core/post.html'

    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        liked_this_post=False
        try:
            post = Post.objects.get(pk=post_id)
            if post_id in request.user.like_set.values_list('post__pk', flat=True):
                liked_this_post=True
        except Exception as e:
            # Return a response with unable to delete
            return HttpResponse('<h1>Sorry, this page isn\'t available.</h1>')
        
        context = { 'post': post, 'liked_this_post': liked_this_post }
        return render(request, self.template_name, context=context)


class LikedPostsView(View):
    template_name = 'core/liked_posts.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class PostCreateView(View):
    form_class = PostCreateForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')


class PostDeleteView(View):

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        try:
            post = Post.objects.get(pk=post_id)
            post.delete()
        except Exception as e:
            # Return a response with unable to delete
            pass
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class PostsExploreView(View):
    template_name = 'core/explore.html'

    def get(self, request, *args, **kwargs):
        all_posts = Post.objects.annotate(count=Count('like')).order_by('-count')
        context = { 'all_posts': all_posts }
        return render(request, self.template_name, context=context)


class FollowDoneVideo(View):

    def post(self, request, *args, **kwargs):
        followed_user_id = request.POST.get('followed_user_id')
        followed_user = User.objects.get(pk=followed_user_id)

        try:
            follow_obj = Follow.objects.get(
                user=request.user,
                follows=followed_user
                )
        except Exception as e:
            follow_obj = Follow.objects.create(follows=followed_user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class UnfollowDoneVideo(View):

    def post(self, request, *args, **kwargs):
        unfollowed_user_id = request.POST.get('unfollowed_user_id')
        unfollowed_user = User.objects.get(pk=unfollowed_user_id)

        try:
            follow_obj = Follow.objects.get(
                user=request.user,
                follows=unfollowed_user
                )
            follow_obj.delete()
        except Exception as e:
            pass

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class PostLikeView(View):

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        post = Post.objects.get(pk=post_id)

        try:
            like_obj = Like.objects.get(user=request.user, post=post)
        except Exception as e:
            like_obj = Like.objects.create(
                user=request.user,
                post=post
                )

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class PostDislikeView(View):

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        post = Post.objects.get(pk=post_id)

        try:
            like_obj = Like.objects.get(user=request.user, post=post)
            like_obj.delete()
        except Exception as e:
            pass

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class PostCommentView(View):

    def post(self, request, *args, **kwargs):
        comment_text = request.POST.get('comment_text')
        post_id = kwargs.get('id')
        post = Post.objects.get(pk=post_id)
        comment_obj = Comment.objects.create(text=comment_text,post=post)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))