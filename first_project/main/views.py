from django.shortcuts import render


# request за замовчуванням
# 'notes/index.html' - шлях до сторінки яку виводимо
# {'title':'Main page'} створюємо шаблон в html( там {{ title }} ) і передаемо у словнику контекст (може бути багато пар)
# title ключ який буде у html, його значення це те що буде відображано на сторінці

def index(request):
    content = {'title':'Main page!',
               'values':['Hello', 'Some', '1234'],
               'obj': {
                   'car' : 'BMW',
                   'age' : '18',
                   'hobby': 'football'
               }
               }
    return render(request, 'main/index.html', content )



def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')

