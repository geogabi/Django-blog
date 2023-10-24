from django import forms
from .models import Article
from ckeditor.fields import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','summary', 'contents','blog_picture')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'summary':forms.TextInput(attrs={'class':'form-control'}),
            'contents': CKEditorWidget(),
        }
