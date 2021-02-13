from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.db.models import Q

from user.forms import UserEditForm
# Create your views here.

User = get_user_model()

class ProfileView(View):
    template_name = 'user/profile.html'
    
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        follows_this_user = False
        try:
            user = User.objects.get(username=username)
            for following in request.user.follow_user.all():
                if following.follows == user:
                    follows_this_user = True
        except Exception as e:
            return HttpResponse('<h1>Sorry, this page isn\'t available.</h1>')

        context = {'user': user, 'follows_this_user': follows_this_user}
        return render(request, self.template_name, context=context)


class ProfileEditView(View):
    template_name = 'user/profile_edit.html'
    form_class = UserEditForm
    
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')

        if request.user.username != username:
            return HttpResponse('<h1>Sorry, this page isn\'t available.</h1>')
        
        context = { 'form': self.form_class(instance=request.user) }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile_edit_view', request.user.username)
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'

            context = { 'form': form }
            return render(request, self.template_name, context)


class AllProfilesView(View):
    template_name = 'user/all_profiles.html'
    
    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('s')
        if not search_term:
            all_profiles = User.objects.filter(is_active=True).values(
                'picture', 'full_name', 'bio', 'username'
                )
        else:
            all_profiles = User.objects.filter(
                    is_active=True
                ).filter(
                    Q(username__contains=search_term) | Q(full_name__contains=search_term)
                ).values(
                    'picture', 'full_name', 'bio', 'username'
                )

        context = {'all_profiles': all_profiles}
        return render(request, self.template_name, context=context)