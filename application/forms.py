from django import forms
from .models import Article
from ckeditor.fields import CKEditorWidget


class CreateNewArticle(forms.Form):

    title = forms.CharField(label='Title', max_length=200)
    slug = forms.SlugField(label='Slug', max_length=300)
    summary = forms.CharField(label='Summary', max_length=200)
    content = forms.CharField(widget=CKEditorWidget())

class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','summary', 'contents')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug':forms.TextInput(attrs={'class': 'form-control'}),
            'summary':forms.TextInput(attrs={'class':'form-control'}),
            'contents': CKEditorWidget()
        }
