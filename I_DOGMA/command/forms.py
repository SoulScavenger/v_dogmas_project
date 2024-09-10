from django import forms

from command.models import Command


class CommandForm(forms.ModelForm):
    """Класс-Форма для модели Post."""

    class Meta:
        model = Command
        exclude = ('author',)
        widgets = {
            'description': forms.Textarea({'cols': '22', 'rows': '5'}),
        }
