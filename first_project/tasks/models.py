from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField('Name',max_length=50)
    description = models.TextField('Description')
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self): # потрібний метод для перенаправлення після внесення змін
        return f'/tasks/'


    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

