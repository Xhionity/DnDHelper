from django.db import models


class Classes(models.Model):
    class_name = models.CharField(max_length=30, verbose_name='Название класса')
    class_description = models.TextField(verbose_name='Описание')
    class_dice = models.CharField(max_length=10, verbose_name='Кость хитов')
    class_mainstat = models.CharField(max_length=40, verbose_name='Основная характеристика')
    class_saving_throws = models.CharField(max_length=40, verbose_name='Владение спасбросками')
    class_equipment = models.TextField(verbose_name='Владение доспехами и оружием')

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Spells(models.Model):
    spell_name = models.CharField(max_length=50, verbose_name='Название заклинания')
    spell_lvl = models.IntegerField(verbose_name='Уровень заклинания')
    spell_duration = models.CharField(max_length=50, verbose_name='Длительность')
    spell_range = models.CharField(max_length=50, verbose_name='Дистанция')
    spell_component = models.CharField(max_length=100, verbose_name='Компоненты')
    spell_school = models.CharField(max_length=20, verbose_name='Школа')
    spell_timecast = models.CharField(max_length=50, verbose_name='Время накладывания')
    spell_description = models.TextField(verbose_name='Описание заклинания')
    spell_class = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name='Доступный класс')

    def __str__(self):
        return f'{self.spell_name} | Уровень: {self.spell_lvl} | {self.spell_class}'

    class Meta:
        verbose_name = 'Заклинание'
        verbose_name_plural = 'Заклинания'
        ordering = ['spell_class', 'spell_lvl', 'spell_name']


class Trinkets(models.Model):
    dice = models.IntegerField(verbose_name='d100')
    value = models.TextField(verbose_name='Безделушка')

    class Meta:
        verbose_name = 'Безделушка'
        verbose_name_plural = 'Безделушки'
        ordering = ['id']

    def __str__(self):
        return f'{self.dice} {self.value}'
