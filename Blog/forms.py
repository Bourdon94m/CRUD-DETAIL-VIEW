from django import forms
from Blog.models import BlogPost

class BlogPostForms(forms.ModelForm):

    class Meta:
        model = BlogPost