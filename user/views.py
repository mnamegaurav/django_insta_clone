from django.shortcuts import render
from django.views.generic import View

from user.forms import UserEditForm
# Create your views here.


class ProfileView(View):
    template_name = 'user/profile.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ProfileEditView(View):
    template_name = 'user/profile_edit.html'
    form_class = UserEditForm
    
    def get(self, request, *args, **kwargs):
        context = { 'form': self.form_class(instance=request.user) }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass