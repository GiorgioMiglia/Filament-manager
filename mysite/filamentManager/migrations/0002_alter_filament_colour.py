# Generated by Django 5.0.3 on 2024-03-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filamentManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filament',
            name='colour',
            field=models.CharField(max_length=30),
        ),
    ]
