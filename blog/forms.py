from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

# filter foreign key, form validation, perbedaan queryset, form form validation
