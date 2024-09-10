from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


def func_rename(newname):
    """Переименовать функцию."""
    def decorator(func):
        func.__name__ = newname
        return func
    return decorator


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тега')

    slug = models.SlugField(
        blank=True,
        verbose_name='Идентификатор'
    )

    class Meta:
        default_related_name = 'tags'
        ordering = ('-id', )
        verbose_name = 'тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Command(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название команды')
    syntax = models.CharField(max_length=255, verbose_name='Синтаксис команды')
    description = models.TextField(verbose_name='Подробное описание')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    image = models.ImageField(upload_to='command_images',
                              blank=True,
                              verbose_name='Изображение',
                              )

    author = models.ForeignKey(
        to=User,
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор',
    )

    tags = models.ManyToManyField(
        to=Tag,
        blank=True,
        verbose_name='Тег'
    )

    @func_rename(newname='Теги')
    def get_tags(self):
        result = ', '.join([str(tag) for tag in self.tags.all()])
        return result

    class Meta:
        default_related_name = 'commands'
        ordering = ('-id',)
        verbose_name = 'команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.name
