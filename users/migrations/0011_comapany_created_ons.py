# Generated by Django 4.2.6 on 2023-11-30 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_car_car_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='comapany',
            name='created_ons',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
