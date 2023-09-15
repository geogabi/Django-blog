from django import forms
from .models import Articol
from ckeditor.fields import CKEditorWidget
class CreateNewArticle(forms.Form):

    title = forms.CharField(label='Title', max_length=200)
    slug = forms.CharField(label='Adress', max_length=50)
    summary = forms.CharField(label='Summary', max_length=100)
    # content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'rows':10}))
    content = forms.CharField(widget=CKEditorWidget())


class EditItem(forms.Form):
    title = forms.CharField(label='Title', max_length=200)
    content = forms.CharField(widget=CKEditorWidget(), empty_value=Articol.contents)

class PostForm(forms.ModelForm):
    class Meta:
        model= Articol
        fields = ('title','contents')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'contents': forms.Textarea(attrs={'class': 'form-control'})
        }


