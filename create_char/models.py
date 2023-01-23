from django.db import models
from base import models as m
# Create your models here.


class Char(models.Model):
    char_name = models.CharField(max_length=30, verbose_name='Имя персонажа')
    char_race = models.ForeignKey(m.Races, on_delete=models.PROTECT, verbose_name='Раса')
    char_class = models.ForeignKey(m.Classes, on_delete=models.PROTECT, verbose_name='Класс')
    char_disc = models.TextField(verbose_name='Описание персонажа')

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'

    def __str__(self):
        return self.char_name


class Stat(models.Model):
    character = models.ForeignKey(Char, on_delete=models.CASCADE, verbose_name='Характеристики персонажа')
    dexterity = models.IntegerField(verbose_name='Ловкость')
    strenght = models.IntegerField(verbose_name='Сила')
    constitution = models.IntegerField(verbose_name='Телосложение')
    intelligence = models.IntegerField(verbose_name='Интеллект')
    wisdom = models.IntegerField(verbose_name='Мудрость')
    charisma = models.IntegerField(verbose_name='Харизма')

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return f'{self.character}'
