from django.shortcuts import render, redirect
from .models import Article
from .forms import CreateNewArticle, PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def home(response):
    articles_list = Article.objects.all()
    paginate = Paginator(articles_list, 3)
    page = response.GET.get('page')
    articles = paginate.get_page(page)
    return render(response, 'home.html', {'articles': articles})


def index(response, id):
    id_article = Article.objects.get(id=id)
    user = id_article.user
    return render(response, 'index.html',{'article':id_article,'user':user})

def index_slug(response, slug):
    slug_article = Article.objects.filter(slug=slug)
    article = slug_article.first()
    return render(response, 'index.html',{'article':article})


@login_required(login_url='/login')
def view(response):
    return render(response, 'view.html')


@login_required(login_url='/login')
def add_new(response):
    if response.method == 'POST':
        form = CreateNewArticle(response.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            slug = form.cleaned_data['slug']
            summary = form.cleaned_data['summary']
            contents = form.cleaned_data['content']
            article = Article(title=title, slug=slug, summary=summary,contents=contents)
            article.save()
            response.user.article.add(article)
            return redirect('/home/')
        return redirect('/view/')
    else:
        form = CreateNewArticle()
    return render(response, 'add_new.html',{'form':form})


def delete_post(response, id):
    articol = Article.objects.get(id=id)
    articol.delete()
    return redirect('/view/')


def edit(response,id):
    article = Article.objects.get(id=id)
    if response.method == "POST":
        form = PostForm(response.POST)
        if form.is_valid():
            article_title = form.cleaned_data['title']
            article_summary = form.cleaned_data['summary']
            article_content = form.cleaned_data['contents']
            article.title = article_title
            article.summary = article_summary
            article.contents = article_content
            article.save()
            return redirect("/view/")
    else:
        form = PostForm(instance=article)
    return render(response, "edit.html", {
                "title": "Edit",
                "article": article,
                'form': form
            })


def search(request):
    if request.method == "POST":
        search = request.POST['search']
        articles = Article.objects.filter(title__contains=search)
        return render(request,'filter.html',{'articles':articles})
    else:
        return render(request,'filter.html',{})

