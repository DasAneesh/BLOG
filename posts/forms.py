from django import forms


class PostForm(forms.Form):
    title = forms.CharField(
        label='header',
        max_length=128,
    )
    text = forms.CharField(
        label='header',
        max_length=512,
        widget = forms.Textarea,
    ) 