# Generated by Django 4.2.2 on 2024-09-28 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diaryentry',
            options={'verbose_name': 'Запись в дневнике', 'verbose_name_plural': 'Записи в дневнике'},
        ),
        migrations.AddField(
            model_name='diaryentry',
            name='date_of_event',
            field=models.DateField(blank=True, help_text='в формате 2024-01-31', null=True, verbose_name='Дата события'),
        ),
        migrations.AddField(
            model_name='diaryentry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='diary/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='diaryentry',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='diaryentry',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания (записи в БД)'),
        ),
        migrations.AlterField(
            model_name='diaryentry',
            name='updated_ad',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата последнего изменения (записи в БД)'),
        ),
    ]
