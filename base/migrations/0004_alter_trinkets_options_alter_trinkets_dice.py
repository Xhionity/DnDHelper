# Generated by Django 4.1.5 on 2023-01-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_alter_trinkets_options_alter_trinkets_dice"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="trinkets",
            options={
                "ordering": ["id"],
                "verbose_name": "Безделушка",
                "verbose_name_plural": "Безделушки",
            },
        ),
        migrations.AlterField(
            model_name="trinkets",
            name="dice",
            field=models.IntegerField(verbose_name="d100"),
        ),
    ]
