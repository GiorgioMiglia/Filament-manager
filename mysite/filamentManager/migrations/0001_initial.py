# Generated by Django 5.0.3 on 2024-03-07 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(choices=[('PLA', 'PLA'), ('PLACF', 'PLA with carbon fiber'), ('PLAsilk', 'PLA silk'), ('PLA+', 'PLA+ (generic)'), ('PETG', 'PETG'), ('ABS', 'ABS'), ('ASA', 'ASA'), ('TPU', 'TPU'), ('TPE', 'TPE')], max_length=10)),
                ('colour', models.TextField(max_length=30)),
                ('brand', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('print_temperature', models.IntegerField()),
                ('bed_temperature', models.IntegerField()),
                ('flow', models.DecimalField(decimal_places=2, default=0.97, max_digits=3)),
                ('max_flowrate', models.DecimalField(decimal_places=1, default=12, max_digits=3)),
                ('k_value', models.DecimalField(decimal_places=3, max_digits=4)),
                ('purchase_date', models.DateTimeField(verbose_name='Purchase date')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=400)),
                ('Filament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filamentManager.filament')),
            ],
        ),
    ]