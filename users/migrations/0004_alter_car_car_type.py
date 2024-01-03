# Generated by Django 4.2.6 on 2023-11-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_car_car_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Petrol'), (2, 'Deisel'), (3, 'CNG')], max_length=50, null=True),
        ),
    ]
