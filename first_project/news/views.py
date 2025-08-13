from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView # імпортуємо клас для відображення повного вмісту статті



def news_home(request):
    #news = Articles.objects.all() # завдяки цій команді витягуэмо всі записи з таблиці
    #news = Articles.objects.order_by('-date') # сортування по даті публікації
    # news = Articles.objects.order_by('title') # сортування по title публікації
    #news = Articles.objects.order_by('-date')[:1] # лімітоване сортування по даті перше
    news = Articles.objects.order_by('-id') # сортування по id публікації
    return render(request, 'news/index.html', {'news':news})


class NewsDetailView(DetailView):

    model = Articles # модель яка працює зі статтями
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles # описуємо з якою таблицею ми працюємо
    template_name = 'news/update.html'
    #fields = ['title', 'anons', 'content', 'date'] # вказуємо поля які будуть доступні для редагування але вигляд не дуже тому ->
    form_class = ArticleForm # підгружаемо клас з формами з forme.py який описували замість html


class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/delete.html'
    success_url = '/news/' # юрл адреса куди переадресується юзер після успішного видалення
    context_object_name = 'article'


def create(request):
    error = ""
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Помилка у формі"
    else:
        form = ArticleForm()

    data = {'form':form, 'error':error }
    return render(request, 'news/create.html', data)
