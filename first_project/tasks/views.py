from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from .forms import TaskForm
from .models import Task



def index2(request):
    #tasks = Task.objects.all()
    #print("Tasks in database:", tasks)  # Друкуємо перелік завдань для перевірки

    # tasks = Task.objects.order_by('title') сортировка по назві, можна по любому полю таблиці
    # також можна використовувати фільтри зрізи Task.objects.order_by('title')[:5] вибираємо перші 5
    tasks = Task.objects.order_by('-id')
    return render(request, 'tasks/index.html', {'title': 'Main page of the task page', 'tasks': tasks})


def create(request):
    error = ""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
        else:
            error = "Помилка у формі"
    else:
        form = TaskForm()

    context = {'form': form, 'error': error}

    return render(request, 'tasks/create.html', context)


class TaskUpdateView(UpdateView):
    model = Task # описуємо з якою таблицею ми працюємо
    template_name = 'tasks/update.html'
    #fields = ['title', 'anons', 'content', 'date'] # вказуємо поля які будуть доступні для редагування але вигляд не дуже тому ->
    form_class = TaskForm # підгружаемо клас з формами з forme.py який описували замість html

    def get(self, request, *args, **kwargs):
        print(f"PK received: {kwargs.get('pk')}")  # Дебагуємо значення pk
        return super().get(request, *args, **kwargs)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = '/tasks/' # юрл адреса куди переадресується юзер після успішного видалення
    context_object_name = 'task'

