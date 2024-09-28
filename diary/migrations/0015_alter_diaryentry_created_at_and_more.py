# Generated by Django 4.2.2 on 2024-09-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0014_alter_diaryentry_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryentry',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания (записи в БД)'),
        ),
        migrations.AlterField(
            model_name='diaryentry',
            name='date_of_event',
            field=models.DateField(blank=True, help_text='в формате 2024-01-31', null=True, verbose_name='Дата события'),
        ),
        migrations.AlterField(
            model_name='diaryentry',
            name='updated_ad',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата последнего изменения (записи в БД)'),
        ),
    ]
