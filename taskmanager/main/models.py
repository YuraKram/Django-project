from django.db import models


class Task(models.Model):
    title = models.CharField('Имя пользователя', max_length=50)
    task = models.TextField('Комментарий')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'


