from django.shortcuts import render, redirect
from .models import Articol
from .forms import CreateNewArticle, PostForm
from django.contrib.auth.decorators import login_required


def home(response):
    articol = Articol.objects.all()
    if response.method == 'POST':
        nota_search = response.POST['search']
        for cuvant in articol:
            lista = cuvant.title.split(' ')
            if nota_search in lista:
                return redirect(f'search/{cuvant.title}')
        if len(nota_search) != 0:
            return redirect(f'search/{nota_search}')
        return redirect('/')
    return render(response, 'aplicatie/home.html', {'articole': articol})


def index(response, id):
    articol = Articol.objects.get(id=id)
    user = articol.user
    return render(response, 'aplicatie/selectare.html',{'articol':articol,'user':user})

def index_slug(response, slug):
    articol = Articol.objects.filter(slug=slug)
    artic = articol.first()
    return render(response, 'aplicatie/selectare.html',{'articol':artic})


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
            contents = form.cleaned_data['content']
            article = Articol(title=title, slug=slug, summary=summary,contents=contents)
            article.save()
            response.user.article.add(article)
            return redirect('/home/')
        return redirect('/view/')
    else:
        form = CreateNewArticle()
    return render(response, 'aplicatie/adauga.html',{'form':form})


def delete_post(response, id):
    articol = Articol.objects.get(id=id)
    articol.delete()
    return redirect('/view/')


def editare(response,id):
    articol = Articol.objects.get(id=id)
    if response.method == "POST":
        form = PostForm(response.POST)
        if form.is_valid():
            articol_title = form.cleaned_data['title']
            articol_continut = form.cleaned_data['contents']
            articol.title = articol_title
            articol.contents = articol_continut
            articol.save()
            return redirect("/view/")
    else:
        form = PostForm(instance=articol)
    return render(response, "aplicatie/edit.html", {
                "titlu": "Editeaza",
                "articol": articol,
                'form': form
            })


def filtru(request,text):
  cuvant = Articol.objects.filter(title=text).all()
  return render(request,'aplicatie/filtru.html',{'cuvant':cuvant})