from django.db import models

# створюємо модель на базі якої буде таблиця в бд

class Articles(models.Model):
    title = models.CharField("Назва новини", max_length=50)
    anons = models.CharField("Анонс", max_length=250)
    content = models.TextField("Новина")
    date = models.DateTimeField("Дата публікації")  #(auto_now_add=True)


    # завдяки методу виводимо тайтл новини
    # тепер вивід такий <QuerySet [<Articles: Новина: some>, <Articles: Новина: UK....
    def __str__(self):
        return f'Новина: {self.title}'


    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'