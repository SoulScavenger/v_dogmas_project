from django.contrib import admin

from command.models import Command, Tag

admin.site.empty_value_display = 'Не задано'


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'syntax', 'description', 'created_at', 'author', 'get_tags'
    )
    list_editable = ('syntax', 'description')
    search_fields = ('name', 'author__username', 'tags__name')
    list_filter = ('tags__name',)
    filter_horizontal = ('tags',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )
