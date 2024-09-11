from django.db import models


class OptimalCommandManager(models.Manager):
    """Кастомный менеджер для модели Command."""

    def get_queryset(self) -> models.QuerySet:
        """Получить отфильтрованный QuerySet."""
        return super().get_queryset().prefetch_related(
            'tags'
        ).select_related('author')
