# Generated by Django 4.2.6 on 2023-11-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_role_id_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.CharField(blank=True, choices=[(1, 'Petrol'), (2, 'Deisel'), (3, 'CNG')], max_length=50, null=True),
        ),
    ]
