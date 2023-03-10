# Generated by Django 4.1.5 on 2023-01-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0011_abilities_racelist_races"),
    ]

    operations = [
        migrations.AddField(
            model_name="races",
            name="race_speed",
            field=models.TextField(blank=True, verbose_name="Скорость"),
        ),
        migrations.AlterField(
            model_name="races",
            name="race_abilities",
            field=models.ManyToManyField(
                blank=True, to="base.abilities", verbose_name="Особенности"
            ),
        ),
    ]
