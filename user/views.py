from django.shortcuts import render, redirect
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
        form = self.form_class(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile_edit_view', request.user.username)
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'

            context = { 'form': form }
            return render(request, self.template_name, context)