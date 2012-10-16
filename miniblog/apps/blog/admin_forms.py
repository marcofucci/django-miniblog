from django import forms
from django.contrib.auth.models import User

from tinymce.widgets import TinyMCE

from blog.models import Post, Category


class PostAdminForm(forms.ModelForm):
    """
        Post Admin Form.
    """
    summary = forms.CharField(
            widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}),
            help_text='Blog post summary.'
        )
    body = forms.CharField(
            widget=TinyMCE(attrs={'cols': 80, 'rows': 20}),
            help_text='Main body.'
        )
    author = forms.ModelChoiceField(
            queryset=User.objects.filter(is_staff=True),
            help_text='Author of this blog post.'
        )

    class Meta:
        model = Post


class CategoryAdminForm(forms.ModelForm):
    """
        Category Admin Form.
    """
    description = forms.CharField(
            required=False,
            widget=TinyMCE(attrs={'cols': 80, 'rows': 10}),
            help_text='This will appear on the posts list.'
        )

    class Meta:
        model = Category