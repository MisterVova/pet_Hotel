# Generated by Django 3.1 on 2022-04-11 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destiny', models.CharField(max_length=64, verbose_name='Предназначение')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('template', models.TextField(blank='', null=True, verbose_name='HTML Шаблон')),
                ('slug', models.SlugField(blank=True, default='', max_length=150, unique=True, verbose_name='ЧПУ')),
            ],
            options={
                'verbose_name': 'Шаблон',
                'verbose_name_plural': 'Шаблоны',
                'ordering': ('destiny', 'title'),
            },
        ),
    ]
