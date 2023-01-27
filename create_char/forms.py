from django.forms import ModelForm, TextInput, IntegerField
from .models import Char, Stat


class CharForm(ModelForm):
    class Meta:
        model = Char
        fields = ['char_name', 'char_view', 'char_history']

        widgets = {
            'char_name': TextInput(attrs={
                'class': 'form',
                'placeholder': 'Имя персонажа'
            }),
            'char_view': TextInput(attrs={
                'class': 'form',
                'placeholder': 'Внешность персонажа'
            }),
            'char_history': TextInput(attrs={
                'class': 'form',
                'placeholder': 'История персонажа'
            })
        }

"""
Заменить class, когда будет готов css
"""
