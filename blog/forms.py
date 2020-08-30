from django import forms
from .models import Comment
from django.utils.translation import gettext_lazy as _

class EmailPostForm(forms.Form):
    name = forms.CharField(label=_('name'),
                           max_length=25)
    email = forms.EmailField(label=_('email'))
    to = forms.EmailField(label=_('to'))
    comments = forms.CharField(label=_('comments'),
                               required=False,
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    messages = {
        'required': 'لطفا این فیلد را پرکنید',
        'invalid': 'لطفا یک ایمیل معتبر وارد کنید',
    }
    name = forms.CharField(required=True,
                           max_length=50,
                           error_messages=messages,
                           label='نام')
    email = forms.EmailField(error_messages=messages,
                             label='ایمیل')
    body = forms.CharField(required=False,
                           widget=forms.Textarea,
                           error_messages=messages,
                           label='نظر')

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class SearchForm(forms.Form):
    query = forms.CharField()
