# Generated by Django 4.2.16 on 2024-09-11 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('command', '0006_command_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='command',
            name='tags',
            field=models.ManyToManyField(blank=True, to='command.tag', verbose_name='Тег'),
        ),
    ]
