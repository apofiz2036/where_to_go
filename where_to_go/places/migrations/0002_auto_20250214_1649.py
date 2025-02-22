# Generated by Django 3.2.25 on 2025-02-14 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название картинки')),
                ('type_image', models.CharField(choices=[('first_image', 'Первая картинка'), ('second_image', 'Вторая картинка')], max_length=50, verbose_name='тип картинки')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='first_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='places_first', to='places.image', verbose_name='Первая картинка'),
        ),
        migrations.AddField(
            model_name='place',
            name='second_image',
            field=models.ManyToManyField(blank=True, related_name='places_second', to='places.Image', verbose_name='Вторая картинка'),
        ),
    ]
