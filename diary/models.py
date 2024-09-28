from django.db import models
from users.models import User
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class DiaryEntry(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='diary/', verbose_name='Изображение', **NULLABLE)
    date_of_event = models.DateField(verbose_name='Дата события', help_text='в формате 2024-01-31',
                                     default='2024-01-01')
    created_at = models.DateField(auto_now_add=True, **NULLABLE, verbose_name='Дата создания (записи в БД)')
    updated_ad = models.DateField(auto_now_add=True, **NULLABLE, verbose_name='Дата последнего изменения (записи в БД)')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.name} \n {self.description} \n {self.created_at}'

    class Meta:
        verbose_name = 'Запись в дневнике'
        verbose_name_plural = 'Записи в дневнике'
