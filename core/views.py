from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.db.models import Count

from core.models import Post

# Create your views here.
class HomeFeedView(View):
    template_name = 'core/feed.html'

    def get(self, request, *args, **kwargs):
        all_posts = Post.objects.all()
        context = { 'all_posts': all_posts }
        return render(request, self.template_name, context=context)


class LikedPostsView(View):
    template_name = 'core/liked_posts.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


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
    template_name = 'core/feed.html'

    def get(self, request, *args, **kwargs):
        all_posts = Post.objects.annotate(count=Count('like')).order_by('-count')
        context = { 'all_posts': all_posts }
        return render(request, self.template_name, context=context)