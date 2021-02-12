from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Count

from core.models import Post
from core.forms import PostCreateForm

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
        try:
            post = Post.objects.get(pk=post_id)
        except Exception as e:
            # Return a response with unable to delete
            return HttpResponse('<h1>Sorry, this page isn\'t available.</h1>')
        
        context = { 'post': post }
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