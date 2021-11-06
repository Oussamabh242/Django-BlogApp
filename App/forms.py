from django.forms import ModelForm, fields

from .models  import Review

class CommentForm(ModelForm):
    class Meta:
        model = Review
        fields ={'name', 'body'}