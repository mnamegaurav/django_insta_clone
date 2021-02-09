from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'picture',
            'full_name', 
            'username',
            'website',
            'bio',
            'email',
            'phone_number',
            'gender',
            'is_account_private',
            )
        labels = {
            'is_account_private': 'Do you want to make your account private ?'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'picture':
                self.fields[field].widget.attrs.update({'class': 'form-control-file'})
            elif field == 'is_account_private':
                self.fields[field].widget.attrs.update({'class': 'form-check-input'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control form-control-sm'})
