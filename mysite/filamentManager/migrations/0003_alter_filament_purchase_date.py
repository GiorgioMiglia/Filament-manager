# Generated by Django 5.0.3 on 2024-03-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filamentManager', '0002_alter_filament_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filament',
            name='purchase_date',
            field=models.DateField(verbose_name='Purchase date'),
        ),
    ]