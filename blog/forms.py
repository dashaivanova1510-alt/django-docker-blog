from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'author_name']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user and self.user.is_authenticated:
            self.fields['author_name'].widget = forms.HiddenInput()
            self.fields['author_name'].required = False
        else:
            self.fields['author_name'].label = "Ваше ім'я (обов'язково)"