# Generated by Django 4.2.6 on 2023-12-05 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_car_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.comapany'),
        ),
        migrations.AlterField(
            model_name='car',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_cars', to=settings.AUTH_USER_MODEL),
        ),
    ]