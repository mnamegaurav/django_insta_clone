from django import forms

from core.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'placeholder': 'Caption this...',
            })
