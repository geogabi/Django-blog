from django.shortcuts import render, redirect
from .models import Articol, Item
from .forms import CreateNewArticle, CreateContent
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(response):
    user = response.user
    articol = Articol.objects.all()
    return render(response, 'aplicatie/home.html',{'user':user,'articol':articol})


def index(response, id):
    articol = Articol.objects.get(id=id)
    user = articol.user
    return render(response, 'aplicatie/selectare.html',{'articol':articol,'user':user})


@login_required(login_url='/login')
def view(response):
    return render(response, 'aplicatie/view.html')


@login_required(login_url='/login')
def adauga(response):
    if response.method == 'POST':
        form = CreateNewArticle(response.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            slug = form.cleaned_data['slug']
            summary = form.cleaned_data['summary']
            article = Articol(title=title, slug=slug, summary=summary)
            article.save()
            response.user.article.add(article)
            return redirect('/view')
        return redirect('/add')
    else:
        form = CreateNewArticle()
    return render(response, 'aplicatie/adauga.html',{'form':form})

def delete_post(response, id):
    articol = Articol.objects.get(id=id)
    print(articol)
    articol.delete()
    return redirect('/view')

def edit_post(response, id):
    articol = Articol.objects.get(id=id)
    if response.method == 'POST':
        form = CreateContent(response.POST)
        if form.is_valid():
            text = form.cleaned_data['content']
            articol.item_set.create(contents=text)
    else:
        form = CreateContent()
    return render(response,'aplicatie/editare.html',{'form':form})