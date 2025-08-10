from django.db import models

# створюємо модель на базі якої буде таблиця в бд

class Articles(models.Model):
    title = models.CharField("Назва новини", max_length=50)
    anons = models.CharField("Анонс", max_length=250)
    content = models.TextField("Новина")
    date = models.DateTimeField("Дата публікації")  #(auto_now_add=True)

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'