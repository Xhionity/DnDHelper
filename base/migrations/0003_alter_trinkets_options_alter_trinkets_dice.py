# Generated by Django 4.1.5 on 2023-01-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_trinkets"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="trinkets",
            options={
                "ordering": ["-id"],
                "verbose_name": "Безделушка",
                "verbose_name_plural": "Безделушки",
            },
        ),
        migrations.AlterField(
            model_name="trinkets",
            name="dice",
            field=models.CharField(max_length=3, verbose_name="d100"),
        ),
    ]