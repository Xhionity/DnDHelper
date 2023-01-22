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


class Stats(models.Model):
    stat_name = models.CharField(max_length=20, verbose_name='Характеристика')
    stat_description = models.CharField(max_length=100, verbose_name='Показатель')
    stat_main = models.CharField(max_length=100, verbose_name='Важно для')

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.stat_name


class Conditions(models.Model):
    condition_name = models.CharField(max_length=100, verbose_name='Состояние')
    condition_description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'
        ordering = ['condition_name']

    def __str__(self):
        return self.condition_name


class Creatures(models.Model):
    creature_name = models.CharField(max_length=100, verbose_name='Название')
    creature_description = models.CharField(max_length=100, verbose_name='Описание')
    creature_armor = models.CharField(max_length=100, verbose_name='Класс доспеха')
    creature_hits = models.CharField(max_length=30, verbose_name='Хиты')
    creature_speed = models.CharField(max_length=100, verbose_name='Скорость')
    creature_stats = models.CharField(max_length=100, verbose_name='Характеристики')
    creature_abilities = models.CharField(max_length=100, verbose_name='Навыки')
    creature_specs = models.CharField(max_length=100, verbose_name='Чувства')
    creature_conditions = models.CharField(max_length=100, verbose_name='Состояния', blank=True)
    creature_languages = models.CharField(max_length=100, verbose_name='Языки', blank=True)
    creature_danger = models.CharField(max_length=100, verbose_name='Опасность')
    creature_skills = models.TextField(verbose_name='Способности')
    creature_actions = models.TextField(verbose_name='Действия')

    class Meta:
        verbose_name = 'Существо'
        verbose_name_plural = 'Существа'
        ordering = ['creature_name']

    def __str__(self):
        return self.creature_name
