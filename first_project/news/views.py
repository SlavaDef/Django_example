from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticleForm



def news_home(request):
    #news = Articles.objects.all() # завдяки цій команді витягуэмо всі записи з таблиці
    #news = Articles.objects.order_by('-date') # сортування по даті публікації
    # news = Articles.objects.order_by('title') # сортування по title публікації
    #news = Articles.objects.order_by('-date')[:1] # лімітоване сортування по даті перше
    news = Articles.objects.order_by('-id')
    return render(request, 'news/index.html', {'news':news})


def create(request):
    error = ""
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
    else:
        error = "Помилка у формі"

    form = ArticleForm()

    data = {'form':form, 'error':error }
    return render(request, 'news/create.html', data)
