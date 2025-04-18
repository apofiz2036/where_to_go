# Generated by Django 3.2.25 on 2025-03-19 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_rename_lan_place_lat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='first_image',
        ),
        migrations.RemoveField(
            model_name='place',
            name='second_image',
        ),
        migrations.AddField(
            model_name='image',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place'),
        ),
    ]
