from django.shortcuts import render
from django.views.generic import View

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