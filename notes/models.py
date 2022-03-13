from django.db import models

class Notes(models.Model):
    user_id = models.IntegerField('Номер пользователя:')
    title = models.CharField('Название', max_length=64)
    date = models.CharField('Дата создания:', max_length=64)

    def get_absolute_url(self):
        return '/notes'

    def __str__(self):
        return self.title


