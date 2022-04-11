# Generated by Django 3.1 on 2022-04-11 19:09

from django.db import migrations, models
import django.db.models.deletion
import garpix_utils.file.file_field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garpix_page', '0001_initial'),
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_date', models.DateTimeField(verbose_name='Дата заезда')),
                ('departure_date', models.DateTimeField(verbose_name='Дата выезда')),
                ('adults', models.PositiveSmallIntegerField(verbose_name='Взрослые')),
                ('children', models.PositiveSmallIntegerField(verbose_name='Дети')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирования',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Рекомендация',
                'verbose_name_plural': 'Рекомендации',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to=garpix_utils.file.file_field.get_file_path, verbose_name='Картинка')),
                ('recommendations', models.ManyToManyField(blank=True, related_name='reasons', to='home.Recommendation', verbose_name='Рекомендации')),
            ],
            options={
                'verbose_name': 'Причина',
                'verbose_name_plural': 'Причины',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
                ('heading', models.TextField(verbose_name='Заголовок')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('html_template', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='template_HomePage', to='show.template', verbose_name='html_template')),
                ('reason', models.ManyToManyField(related_name='reasons_HomePage', to='home.Reason', verbose_name='Reason')),
            ],
            options={
                'verbose_name': 'HomePage',
                'verbose_name_plural': 'HomePages',
                'ordering': ('-created_at',),
            },
            bases=('garpix_page.basepage',),
        ),
    ]
