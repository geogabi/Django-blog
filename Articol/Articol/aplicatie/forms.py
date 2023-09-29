from django import forms
from .models import Articol
from ckeditor.fields import CKEditorWidget


class CreateNewArticle(forms.Form):

    title = forms.CharField(label='Title', max_length=200)
    slug = forms.CharField(label='Slug', max_length=50)
    summary = forms.CharField(label='Summary', max_length=100)
    content = forms.CharField(widget=CKEditorWidget())

class PostForm(forms.ModelForm):
    class Meta:
        model = Articol
        fields = ('title', 'contents')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'contents': CKEditorWidget()
        }
