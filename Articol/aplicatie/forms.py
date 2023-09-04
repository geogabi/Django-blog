from django import forms


class CreateNewArticle(forms.Form):

    title = forms.CharField(label='Title', max_length=200)
    slug = forms.CharField(label='Adress', max_length=50)
    summary = forms.CharField(label='Summary', max_length=100)

class CreateContent(forms.Form):

    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'rows':10}))

