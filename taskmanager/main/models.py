from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Задача')
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.id}'
    
    class  Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
