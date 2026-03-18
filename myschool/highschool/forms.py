from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "published"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "w-full border rounded px-3 py-2"}),
            "content": forms.Textarea(attrs={"class": "w-full border rounded px-3 py-2 h-40"}),
            "published": forms.CheckboxInput(attrs={"class": "mr-2"}),
        }
